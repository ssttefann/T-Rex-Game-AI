import pygame
import random


class TreeObstacle(pygame.sprite.Sprite):
    """ Tree-like obstacle

        Attributes
        ------------
        image : pygame.Surface
            image of the object
        rect : rectangle
            area which object covers on game surface
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("..\\img\\tree" + str(random.randint(1,5))+ ".png")
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()

    def update(self, *args):
        """ Code to be executed to update the Tree obstacle during each frame of the game

            Attributes
            ------------
            args : float
                number of pixel to move the object
        """
        self.rect.x -= args[0]


class BirdObstacle(pygame.sprite.Sprite):
    """ Bird obstacle

        Attributes
        ------------
        images : list {pygame.Surface}
            all possible images of an object
        image : pygame.Surface
            current image of the object
        index : int
            index of current image from images
        last_update : int
            time of a last image change
        rect : rectangle
            area which object covers on game surface
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = [pygame.image.load("..\\img\\bird0.png").convert(), pygame.image.load("..\\img\\bird1.png").convert()]
        self.image = self.images[1]
        self.index = 0
        self.last_update = pygame.time.get_ticks()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

    def update(self, *args):
        """ Code to be executed to update the Bird obstacle during each frame of the game

            Attributes
            ------------
            args : float
                number of pixel to move the object
        """

        # change picture every 100 milliseconds
        now = pygame.time.get_ticks()
        if now - self.last_update > 100:
            self.index = self.index ^ 1
            self.image = self.images[self.index]
            self.last_update = now
            prom = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = prom

        self.rect.x -= args[0]
