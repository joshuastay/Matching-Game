import pygame
import random
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()
WIDTH = 0
HEIGHT = 0
x = -200
y = random.randrange(1000)
game_screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
game_surface = pygame.Surface((100, 100))
game_surface.fill((255, 255, 255))

foods = pygame.image.load('Food Pack.png')
foods = pygame.transform.scale(foods, (256, 640))
clouds = pygame.image.load('cloud.png')
clouds = pygame.transform.scale(clouds, (168, 96) )
food_dict = {'chicken': (128, 0, 64, 64), 'donut': (192, 0, 64, 64),
             'apple': (64, 0, 64, 64), 'banana': (64, 64, 64, 64),
             'strawberry': (64, 192, 64, 64), 'sushi': (128, 192, 64, 64),
             'watermelon': (64, 256, 64, 64), 'egg': (128, 256, 64, 64),
             'fries': (128, 320, 64, 64), 'hamburger': (128, 384, 64, 64)}

running = True

while running:
    x += 1
    if x > 2000:
        x = -200
        y = random.randrange(1000)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False
    game_screen.fill((51, 204, 255))
    game_screen.blit(clouds, (x, y), (0, 0, 168, 96))
    game_screen.blit(foods, (330, 100), food_dict['chicken'])
    game_screen.blit(foods, (630, 100), food_dict['donut'])
    game_screen.blit(foods, (930, 100), food_dict['apple'])
    game_screen.blit(foods, (1230, 100), food_dict['banana'])
    game_screen.blit(foods, (1530, 100), food_dict['strawberry'])
    game_screen.blit(foods, (330, 350), food_dict['sushi'])
    game_screen.blit(foods, (630, 350), food_dict['watermelon'])
    game_screen.blit(foods, (930, 350), food_dict['egg'])
    game_screen.blit(foods, (1230, 350), food_dict['fries'])
    game_screen.blit(foods, (1530, 350), food_dict['hamburger'])
    game_screen.blit(foods, (330, 600), food_dict['hamburger'])
    game_screen.blit(foods, (630, 600), food_dict['fries'])
    game_screen.blit(foods, (930, 600), food_dict['egg'])
    game_screen.blit(foods, (1230, 600), food_dict['watermelon'])
    game_screen.blit(foods, (1530, 600), food_dict['sushi'])
    game_screen.blit(foods, (330, 850), food_dict['strawberry'])
    game_screen.blit(foods, (630, 850), food_dict['banana'])
    game_screen.blit(foods, (930, 850), food_dict['apple'])
    game_screen.blit(foods, (1230, 850), food_dict['donut'])
    game_screen.blit(foods, (1530, 850), food_dict['chicken'])

    pygame.display.flip()

pygame.quit()
