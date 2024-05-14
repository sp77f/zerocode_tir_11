import pygame
import random
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/icon1.png")
pygame.display.set_icon(icon)
target = pygame.image.load("img/apple.png")
target_width = 50
target_height = 50

target_x = random.randint(0, screen_width - target_width)
target_y = random.randint(0, screen_height - target_height)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
score = 0
speed = 25
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            if target_x <= mouse_x <= target_x + target_width and target_y <= mouse_y <= target_y + target_height:
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                screen.fill(color)
                target_x = random.randint(0, screen_width - target_width)
                target_y = random.randint(0, screen_height - target_height)
                score += 1
    screen.blit(target, (target_x, target_y))
    text = font.render(f'Очки: {score}', True, (255, 255, 255))
    screen.blit(text, (10, 10))
    target_x += random.randint(-speed, speed)
    target_y += random.randint(-speed, speed)
    if target_x < 0:
        target_x = 0
    elif target_x > screen_width - target_width:
        target_x = screen_width - target_width
    if target_y < 0:
        target_y = 0
    elif target_y > screen_height - target_height:
        target_y = screen_height - target_height
    pygame.display.update()
    clock.tick(2)
pygame.quit()
