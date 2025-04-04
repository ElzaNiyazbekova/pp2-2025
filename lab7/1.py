
import pygame
import time

pygame.init()

clock_img = pygame.image.load("/Users/elzaniyazbekova/Desktop/pp2/lab7/mickeyclock.png")
minute_hand_img = pygame.image.load("/Users/elzaniyazbekova/Desktop/pp2/lab7/hand-1.png")
second_hand_img = pygame.image.load("/Users/elzaniyazbekova/Desktop/pp2/lab7/hand-2 (1).png")

WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 750
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("MickeyClock")

clock = pygame.time.Clock()

running = True


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    current_time = time.localtime()
    
    minute_angle = (current_time.tm_min / 60) * 360
    second_angle = (current_time.tm_sec / 60) * 360
    
    minute_hand_rotated = pygame.transform.rotate(minute_hand_img, minute_angle)
    second_hand_rotated = pygame.transform.rotate(second_hand_img, -second_angle)
    
    window.blit(clock_img, (0, 0))
    
    minute_hand_x = WINDOW_WIDTH / 2 - minute_hand_rotated.get_width() / 2
    minute_hand_y = WINDOW_HEIGHT / 2 - minute_hand_rotated.get_height() / 2
    window.blit(minute_hand_rotated, (minute_hand_x, minute_hand_y))
    
    second_hand_x = WINDOW_WIDTH / 2 -second_hand_rotated.get_width() / 2
    second_hand_y = WINDOW_HEIGHT / 2 - second_hand_rotated.get_height() / 2
    window.blit(second_hand_rotated, (second_hand_x, second_hand_y))
    
    pygame.display.update()
    
    clock.tick(60)
while running:
    for e in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    cur_time = time.localtime()
    min = (cur_time.tm_min/60)*360
    sec = (cur_time.tm_sec/60)*360


pygame.quit()