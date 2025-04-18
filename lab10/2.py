import pygame
import sys
import copy
import random
import time
import psycopg2

print("Enter your name")
name = input()

# Подключение к базе данных
db = psycopg2.connect(
    dbname='lab10',
    user='postgres',
    password='12345',
    host='localhost',
    port='5432'
)
current = db.cursor()

# Создание таблицы
sql = """
    CREATE TABLE IF NOT EXISTS Scores(
        player_name VARCHAR,
        player_score VARCHAR
    );
"""
current.execute(sql)
db.commit()

pygame.init()

scale = 10
score = 0
level = 0
SPEED = 10

food_x = 10
food_y = 10

bomb_x = 15
bomb_y = 15

display = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

background = (0, 0, 0)
snake_colour = (255, 137, 0)
food_colour = (0, 255, 0)
bomb_colour = (255, 0, 210)
snake_head = (255, 247, 0)
font_colour = (255, 255, 255)
defeat_colour = (255, 0, 0)

class Snake:
    def __init__(self, x_start, y_start):
        self.x = x_start
        self.y = y_start
        self.w = 10
        self.h = 10
        self.x_dir = 1
        self.y_dir = 0
        self.history = [[self.x, self.y]]
        self.length = 1

    def reset(self):
        self.x = 500 / 2 - scale
        self.y = 500 / 2 - scale
        self.x_dir = 1
        self.y_dir = 0
        self.history = [[self.x, self.y]]
        self.length = 1

    def show(self):
        for i in range(self.length):
            color = snake_head if i == 0 else snake_colour
            pygame.draw.rect(display, color, (self.history[i][0], self.history[i][1], self.w, self.h))

    def check_eaten(self):
        return abs(self.history[0][0] - food_x) < scale and abs(self.history[0][1] - food_y) < scale

    def check_bomb(self):
        return abs(self.history[0][0] - bomb_x) < scale and abs(self.history[0][1] - bomb_y) < scale

    def level(self):
        return (self.length - 1) // 5

    def grow(self):
        self.length += 1
        self.history.append(self.history[self.length - 2])

    def death(self):
        for i in range(1, self.length):
            if self.history[0] == self.history[i] and self.length > 2:
                return True
        return False

    def update(self):
        # Update the head position
        new_head = [self.history[0][0] + self.x_dir * scale, self.history[0][1] + self.y_dir * scale]
        self.history.insert(0, new_head)
        if len(self.history) > self.length:
            self.history.pop()

class Food:
    def new_location(self):
        global food_x, food_y
        food_x = random.randrange(1, 500 // scale - 1) * scale
        food_y = random.randrange(1, 500 // scale - 1) * scale

    def show(self):
        pygame.draw.rect(display, food_colour, (food_x, food_y, scale, scale))

class Bomb:
    def new_location(self):
        global bomb_x, bomb_y
        bomb_x = random.randrange(1, 500 // scale - 1) * scale
        bomb_y = random.randrange(1, 500 // scale - 1) * scale

    def show(self):
        pygame.draw.rect(display, bomb_colour, (bomb_x, bomb_y, scale, scale))

def show_score():
    font = pygame.font.SysFont(None, 20)
    text = font.render("Score: " + str(score), True, font_colour)
    display.blit(text, (scale, scale))

def show_level():
    font = pygame.font.SysFont(None, 20)
    text = font.render("Level: " + str(level), True, font_colour)
    display.blit(text, (90 - scale, scale))

def show_name():
    font = pygame.font.SysFont(None, 20)
    text = font.render("Player: " + name, True, font_colour)
    display.blit(text, (350 - scale, scale))

def gameLoop():
    global score, level, SPEED

    snake = Snake(500 / 2, 500 / 2)
    food = Food()
    food.new_location()
    bomb = Bomb()
    bomb.new_location()

    def defeat(score):
        current.execute("INSERT INTO Scores VALUES(%s, %s);", (name, str(score)))
        db.commit()
        display.fill(background)
        font1 = pygame.font.SysFont(None, 100)
        text1 = font1.render("Game Over!", True, defeat_colour)
        display.blit(text1, (50, 200))
        pygame.display.update()
        time.sleep(3)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_LEFT:
                    snake.x_dir = -1
                    snake.y_dir = 0
                elif event.key == pygame.K_RIGHT:
                    snake.x_dir = 1
                    snake.y_dir = 0
                elif event.key == pygame.K_UP:
                    snake.x_dir = 0
                    snake.y_dir = -1
                elif event.key == pygame.K_DOWN:
                    snake.x_dir = 0
                    snake.y_dir = 1

        snake.update()

        # Проверка на удар об стену
        head_x, head_y = snake.history[0]
        if head_x < 0 or head_x >= 500 or head_y < 0 or head_y >= 500:
            defeat(score)
            break

        if snake.death():
            defeat(score)
            break

        if snake.check_bomb():
            defeat(score)
            break

        if snake.check_eaten():
            food.new_location()
            score += random.randint(1, 5)
            snake.grow()

        new_level = snake.level()
        if new_level > level:
            level = new_level
            SPEED += 3
            food.new_location()
            snake.grow()

        display.fill(background)
        snake.show()
        food.show()
        bomb.show()
        show_score()
        show_level()
        show_name()

        pygame.display.update()
        clock.tick(SPEED)

    # Перезапуск игры
    score = 0
    level = 0
    SPEED = 10
    gameLoop()

gameLoop()