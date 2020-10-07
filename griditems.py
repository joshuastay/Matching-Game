import pygame
import random


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


class CloudHandler:
    def __init__(self, speed, image, image_rect, surface, height, width):
        self.x = -500
        self.speed = speed
        self.height = height
        self.width = width
        self.y = random.randrange(self.height)
        self.image = image
        self.image_rect = image_rect
        self.surface = surface

    def cloud_update(self):
        self.x += self.speed
        if self.x > self.width:
            self.x = -500
            self.y = random.randrange(self.height)

    def background_cloud_draw(self):
        self.surface.blit(self.image, (int(self.x), int(self.y)), self.image_rect)
