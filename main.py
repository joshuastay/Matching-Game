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

cover_rect = pygame.Rect(0, 384, 256, 128)
score = 0


class CloudHandler:
    def __init__(self, speed):
        self.x = -500
        self.speed = speed
        self.y = random.randrange(height)

    def cloud_update(self):
        self.x += self.speed
        if self.x > width:
            self.x = -500
            self.y = random.randrange(height)


class FoodCloud:
    def __init__(self, x, y, food_image, food_rect, cloud_image, cloud_rect, surface):
        self.x = x
        self.y = y
        self.food_image = food_image
        self.food_rect = food_rect
        self.cloud_image = cloud_image
        self.cloud_rect = cloud_rect
        self.surface = surface

    def draw_food(self):
        self.surface.blit(self.food_image, (self.x, self.y), self.food_rect)

    def draw_cloud(self):
        self.surface.blit(self.cloud_image, (self.x - 100, self.y - 32), self.cloud_rect)

    def collision(self, mouse_pos):
        new_rect = pygame.Rect(self.x - 100, self.y - 32, 256, 128)
        return new_rect.collidepoint(mouse_pos)


grid1_1 = FoodCloud(x_foodr1, y_foodr1, foods, food_dict['chicken'], cloud_cover, cover_rect, game_screen)
grid1_2 = FoodCloud(x_foodr2, y_foodr1, foods, food_dict['donut'], cloud_cover, cover_rect, game_screen)
grid1_3 = FoodCloud(x_foodr3, y_foodr1, foods, food_dict['apple'], cloud_cover, cover_rect, game_screen)
grid1_4 = FoodCloud(x_foodr4, y_foodr1, foods, food_dict['banana'], cloud_cover, cover_rect, game_screen)
grid1_5 = FoodCloud(x_foodr5, y_foodr1, foods, food_dict['strawberry'], cloud_cover, cover_rect, game_screen)
grid2_1 = FoodCloud(x_foodr1, y_foodr2, foods, food_dict['sushi'], cloud_cover, cover_rect, game_screen)
grid2_2 = FoodCloud(x_foodr2, y_foodr2, foods, food_dict['watermelon'], cloud_cover, cover_rect, game_screen)
grid2_3 = FoodCloud(x_foodr3, y_foodr2, foods, food_dict['egg'], cloud_cover, cover_rect, game_screen)
grid2_4 = FoodCloud(x_foodr4, y_foodr2, foods, food_dict['fries'], cloud_cover, cover_rect, game_screen)
grid2_5 = FoodCloud(x_foodr5, y_foodr2, foods, food_dict['hamburger'], cloud_cover, cover_rect, game_screen)
grid3_1 = FoodCloud(x_foodr1, y_foodr3, foods, food_dict['hamburger'], cloud_cover, cover_rect, game_screen)
grid3_2 = FoodCloud(x_foodr2, y_foodr3, foods, food_dict['fries'], cloud_cover, cover_rect, game_screen)
grid3_3 = FoodCloud(x_foodr3, y_foodr3, foods, food_dict['egg'], cloud_cover, cover_rect, game_screen)
grid3_4 = FoodCloud(x_foodr4, y_foodr3, foods, food_dict['watermelon'], cloud_cover, cover_rect, game_screen)
grid3_5 = FoodCloud(x_foodr5, y_foodr3, foods, food_dict['sushi'], cloud_cover, cover_rect, game_screen)
grid4_1 = FoodCloud(x_foodr1, y_foodr4, foods, food_dict['strawberry'], cloud_cover, cover_rect, game_screen)
grid4_2 = FoodCloud(x_foodr2, y_foodr4, foods, food_dict['banana'], cloud_cover, cover_rect, game_screen)
grid4_3 = FoodCloud(x_foodr3, y_foodr4, foods, food_dict['apple'], cloud_cover, cover_rect, game_screen)
grid4_4 = FoodCloud(x_foodr4, y_foodr4, foods, food_dict['donut'], cloud_cover, cover_rect, game_screen)
grid4_5 = FoodCloud(x_foodr5, y_foodr4, foods, food_dict['chicken'], cloud_cover, cover_rect, game_screen)

food_list = [grid1_1, grid1_2, grid1_3, grid1_4, grid1_5, grid2_1,
             grid2_2, grid2_3, grid2_4, grid2_5, grid3_1, grid3_2,
             grid3_3, grid3_4, grid3_5, grid4_1, grid4_2, grid4_3,
             grid4_4, grid4_5]

cloud_cover_list = [grid1_1, grid1_2, grid1_3, grid1_4, grid1_5, grid2_1,
                    grid2_2, grid2_3, grid2_4, grid2_5, grid3_1, grid3_2,
                    grid3_3, grid3_4, grid3_5, grid4_1, grid4_2, grid4_3,
                    grid4_4, grid4_5]

reveal_list = list()

cloud1 = CloudHandler(1)
cloud2 = CloudHandler(1.1)
cloud3 = CloudHandler(.5)
cloud4 = CloudHandler(1.5)

cloud_list = [cloud1, cloud2, cloud3, cloud4]

running = True
timer = 0


def clouds_function():
    while running:
        for background_cloud in cloud_list:
            background_cloud.cloud_update()
            #game_screen.blit(clouds, (int(background_cloud.x), background_cloud.y), (0, 0, 168, 96))
            game_screen.blit(cloud_cover, (int(background_cloud.x), background_cloud.y), (0, 0, 512, 128))


while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and len(reveal_list) < 2:
                print('mouse clicked!')
                pos = pygame.mouse.get_pos()
                print(pos)
                timer = 40
                for cloud in cloud_cover_list:
                    if cloud.collision(pos):
                        reveal_list.append(cloud)
                        cloud_cover_list.remove(cloud)

    if timer > 0:
        timer -= 1

    if len(reveal_list) >= 2 and reveal_list[0].food_rect == reveal_list[1].food_rect:
        score += 1
        reveal_list.clear()
    elif len(reveal_list) >= 2 and reveal_list[0].food_rect != reveal_list[1].food_rect and timer == 0:
        for each in reveal_list:
            cloud_cover_list.append(each)
        reveal_list.clear()

    game_screen.fill((51, 204, 255))

    for cloud in cloud_list:
        cloud.cloud_update()
        #game_screen.blit(clouds, (int(cloud.x), cloud.y), (0, 0, 168, 96))
        game_screen.blit(cloud_cover, (int(cloud.x), cloud.y), (0, 128, 512, 128))

    for food in food_list:
        food.draw_food()

    for cloud in cloud_cover_list:
        cloud.draw_cloud()

    pygame.display.flip()

pygame.quit()
