import pygame
import random
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()
WIDTH = 0
HEIGHT = 0

game_screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

width = game_screen.get_width()
height = game_screen.get_height()

game_surface = pygame.Surface((100, 100))
game_surface.fill((255, 255, 255))

foods = pygame.image.load('Food Pack.png')
foods = pygame.transform.scale(foods, (256, 640))
clouds = pygame.image.load('cloud.png')
clouds = pygame.transform.scale(clouds, (168, 96))
cloud_cover = pygame.image.load('cloudcover.png')
cloud_cover = pygame.transform.scale(cloud_cover, (512, 512))
food_dict = {'chicken': (128, 0, 64, 64), 'donut': (192, 0, 64, 64),
             'apple': (64, 0, 64, 64), 'banana': (64, 64, 64, 64),
             'strawberry': (64, 192, 64, 64), 'sushi': (128, 192, 64, 64),
             'watermelon': (64, 256, 64, 64), 'egg': (128, 256, 64, 64),
             'fries': (128, 320, 64, 64), 'hamburger': (128, 384, 64, 64)}

y_foodr1 = int(height * .092)
y_foodr2 = int(height * .324)
y_foodr3 = int(height * .56)
y_foodr4 = int(height * .787)
x_foodr1 = int(width * .172)
x_foodr2 = int(width * .328)
x_foodr3 = int(width * .484)
x_foodr4 = int(width * .641)
x_foodr5 = int(width * .797)


class CloudHandler:
    def __init__(self, speed):
        self.x = -200
        self.speed = speed
        self.y = random.randrange(height)

    def cloud_update(self):
        self.x += self.speed
        if self.x > width:
            self.x = -200
            self.y = random.randrange(height)


class CloudCover:
    def __init__(self, x, y, image, surface, rect_size):
        self.x = x
        self.y = y
        self.image = image
        self.surface = surface
        self.rect_size = rect_size

    def draw(self):
        self.surface.blit(self.image, (self.x, self.y), self.rect_size)

    def collision(self, pos):
        new_rect = pygame.Rect(self.x, self.y, 256, 128)
        return new_rect.collidepoint(pos)


cover_rect = pygame.Rect(0, 384, 256, 128)

cover1 = CloudCover(x_foodr1 - 100, y_foodr1 - 32, cloud_cover, game_screen, cover_rect)
cover2 = CloudCover(x_foodr2 - 100, y_foodr1 - 32, cloud_cover, game_screen, cover_rect)
cover3 = CloudCover(x_foodr3 - 100, y_foodr1 - 32, cloud_cover, game_screen, cover_rect)
cover4 = CloudCover(x_foodr4 - 100, y_foodr1 - 32, cloud_cover, game_screen, cover_rect)
cover5 = CloudCover(x_foodr5 - 100, y_foodr1 - 32, cloud_cover, game_screen, cover_rect)
cover6 = CloudCover(x_foodr1 - 100, y_foodr2 - 32, cloud_cover, game_screen, cover_rect)
cover7 = CloudCover(x_foodr2 - 100, y_foodr2 - 32, cloud_cover, game_screen, cover_rect)
cover8 = CloudCover(x_foodr3 - 100, y_foodr2 - 32, cloud_cover, game_screen, cover_rect)
cover9 = CloudCover(x_foodr4 - 100, y_foodr2 - 32, cloud_cover, game_screen, cover_rect)
cover10 = CloudCover(x_foodr5 - 100, y_foodr2 - 32, cloud_cover, game_screen, cover_rect)
cover11 = CloudCover(x_foodr1 - 100, y_foodr3 - 32, cloud_cover, game_screen, cover_rect)
cover12 = CloudCover(x_foodr2 - 100, y_foodr3 - 32, cloud_cover, game_screen, cover_rect)
cover13 = CloudCover(x_foodr3 - 100, y_foodr3 - 32, cloud_cover, game_screen, cover_rect)
cover14 = CloudCover(x_foodr4 - 100, y_foodr3 - 32, cloud_cover, game_screen, cover_rect)
cover15 = CloudCover(x_foodr5 - 100, y_foodr3 - 32, cloud_cover, game_screen, cover_rect)
cover16 = CloudCover(x_foodr1 - 100, y_foodr4 - 32, cloud_cover, game_screen, cover_rect)
cover17 = CloudCover(x_foodr2 - 100, y_foodr4 - 32, cloud_cover, game_screen, cover_rect)
cover18 = CloudCover(x_foodr3 - 100, y_foodr4 - 32, cloud_cover, game_screen, cover_rect)
cover19 = CloudCover(x_foodr4 - 100, y_foodr4 - 32, cloud_cover, game_screen, cover_rect)
cover20 = CloudCover(x_foodr5 - 100, y_foodr4 - 32, cloud_cover, game_screen, cover_rect)

cover_list = [cover1, cover2, cover3, cover4, cover5, cover6, cover7, cover8, cover9, cover10, cover11, cover12,
              cover13, cover14, cover15, cover16, cover17, cover18, cover19, cover20]
reveal_list = list()

cloud1 = CloudHandler(1)
cloud2 = CloudHandler(1.1)
cloud3 = CloudHandler(.5)
cloud4 = CloudHandler(1.5)

cloud_list = [cloud1, cloud2, cloud3, cloud4]

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

    game_screen.fill((51, 204, 255))

    for cloud in cloud_list:
        cloud.cloud_update()
        game_screen.blit(clouds, (int(cloud.x), cloud.y), (0, 0, 168, 96))

    game_screen.blit(foods, (x_foodr1, y_foodr1), food_dict['chicken'])
    game_screen.blit(foods, (x_foodr2, y_foodr1), food_dict['donut'])
    game_screen.blit(foods, (x_foodr3, y_foodr1), food_dict['apple'])
    game_screen.blit(foods, (x_foodr4, y_foodr1), food_dict['banana'])
    game_screen.blit(foods, (x_foodr5, y_foodr1), food_dict['strawberry'])
    game_screen.blit(foods, (x_foodr1, y_foodr2), food_dict['sushi'])
    game_screen.blit(foods, (x_foodr2, y_foodr2), food_dict['watermelon'])
    game_screen.blit(foods, (x_foodr3, y_foodr2), food_dict['egg'])
    game_screen.blit(foods, (x_foodr4, y_foodr2), food_dict['fries'])
    game_screen.blit(foods, (x_foodr5, y_foodr2), food_dict['hamburger'])
    game_screen.blit(foods, (x_foodr1, y_foodr3), food_dict['hamburger'])
    game_screen.blit(foods, (x_foodr2, y_foodr3), food_dict['fries'])
    game_screen.blit(foods, (x_foodr3, y_foodr3), food_dict['egg'])
    game_screen.blit(foods, (x_foodr4, y_foodr3), food_dict['watermelon'])
    game_screen.blit(foods, (x_foodr5, y_foodr3), food_dict['sushi'])
    game_screen.blit(foods, (x_foodr1, y_foodr4), food_dict['strawberry'])
    game_screen.blit(foods, (x_foodr2, y_foodr4), food_dict['banana'])
    game_screen.blit(foods, (x_foodr3, y_foodr4), food_dict['apple'])
    game_screen.blit(foods, (x_foodr4, y_foodr4), food_dict['donut'])
    game_screen.blit(foods, (x_foodr5, y_foodr4), food_dict['chicken'])

    for each in cover_list:
        each.draw()
    if pygame.mouse.get_pressed()[0]:
        print('mouse clicked!')
        pos = pygame.mouse.get_pos()
        print(pos)
        for cloud in cover_list:
            if cloud.collision(pos):
                cover_list.remove(cloud)

    pygame.display.flip()

pygame.quit()
