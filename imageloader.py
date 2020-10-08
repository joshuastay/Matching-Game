import pygame


class ImageHandler:
    def __init__(self, image, x, y, surface):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.surface = surface
        self.image_width = self.image.get_width()
        self.image_height = self.image.get_height()
        self.image_rect = (self.x, self.y, self.image_width, self.image_height)

    def draw(self):
        self.surface.blit(self.image, (self.x, self.y))

    def resize(self, width, height):
        self.image = pygame.transform.scale(self.image, (int(width * (self.image_width / 2560)),
                                                         int(height * (self.image_height / 1440))))

    def get_rect(self):
        return pygame.Rect(self.image_rect)
