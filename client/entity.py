import pygame
from pygame.locals import *
from globals import *


class Entity(pygame.sprite.Sprite):
    def __init__(self, filename, xsize=50, ysize=50, xinit=SCREEN_WIDTH/2, yinit=SCREEN_HEIGHT/2):
        super().__init__()
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (xsize, ysize))
        self.rect = self.image.get_rect()
        self.rect.center = (xinit, yinit)

    def update_position(self, new_x, new_y):
        self.rect.center = (new_x, new_y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(Entity):
    MOVEMENT_SPEED = 5

    def __init__(self, filename, xsize=50, ysize=50, xinit=0, yinit=0):
        super().__init__(filename, xsize, ysize, xinit, yinit)
        self.has_updated = False

    def update(self):
        pressed_key = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_key[K_LEFT]:
                self.rect.move_ip(-5, 0)
                self.has_updated = True
        if self.rect.right < SCREEN_WIDTH:
            if pressed_key[K_RIGHT]:
                self.rect.move_ip(5, 0)
                self.has_updated = True
        if self.rect.top > 0:
            if pressed_key[K_UP]:
                self.rect.move_ip(0, -5)
                self.has_updated = True
        if self.rect.bottom < SCREEN_HEIGHT:
            if pressed_key[K_DOWN]:
                self.rect.move_ip(0, 5)
                self.has_updated = True

        if self.has_updated:
            self.has_updated = False
            return {"state": "UPDATE_PLAYER_POSITION", "new_x": self.rect.x, "new_y": self.rect.y}
        return None
