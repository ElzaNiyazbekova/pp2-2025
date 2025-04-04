# import pygame

# pygame.init()

# screen_width, screen_height = 500, 500
# screen = pygame.display.set_mode((screen_width, screen_height))

# pygame.display.set_caption("Red Ball")

# ball_radius = 50
# ball_x, ball_y = screen_width // 2, screen_height // 2
# ball_color = (255, 0, 0)

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()

#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP:
#                 ball_y = max(ball_y - 20, ball_radius)
#             elif event.key == pygame.K_DOWN:
#                 ball_y = min(ball_y + 20, screen_height - ball_radius)
#             elif event.key == pygame.K_LEFT:
#                 ball_x = max(ball_x - 20, ball_radius)
            
#             elif event.key == pygame.K_RIGHT:
#                 ball_x = min(ball_x + 20, screen_width - ball_radius)
            


#     screen.fill((255, 255, 255))

 
#     pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

#     pygame.display.update()

import pygame

pygame.init()

screen_width, screen_height = 500, 500
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Red Ball")

tr_s = 50

ball_x, ball_y = screen_width // 2, screen_height // 2
ball_color = (255, 0, 0)
def get_triangle_points(x, y, size):
    return [(x, y - size), (x - size, y + size), (x + size, y + size)]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_y = max(ball_y - 20, tr_s)
            elif event.key == pygame.K_DOWN:
                ball_y = min(ball_y + 20, screen_height -tr_s)
            elif event.key == pygame.K_LEFT:
                ball_x = max(ball_x - 20, tr_s)
            
            elif event.key == pygame.K_RIGHT:
                ball_x = min(ball_x + 20, screen_width - tr_s)
            


    screen.fill((255, 255, 255))

    tr_p = get_triangle_points(ball_x, ball_y, tr_s)
    pygame.draw.polygon(screen, ball_color, (tr_p))

    pygame.display.update()


import pygame

pygame.init()

screen_width, screen_height = 500, 500
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Moving Rectangle")

# Размеры прямоугольника
rect_width, rect_height = 50, 50
rect_x, rect_y = (screen_width - rect_width) // 2, (screen_height - rect_height) // 2
rect_color = (255, 0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rect_y = max(rect_y - 20, 0)  # Верхняя граница
            elif event.key == pygame.K_DOWN:
                rect_y = min(rect_y + 20, screen_height - rect_height)  # Нижняя граница
            elif event.key == pygame.K_LEFT:
                rect_x = max(rect_x - 20, 0)  # Левая граница
            elif event.key == pygame.K_RIGHT:
                rect_x = min(rect_x + 20, screen_width - rect_width)  # Правая граница

    screen.fill((255, 255, 255))

    # Отрисовка прямоугольника
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))

    pygame.display.update()
