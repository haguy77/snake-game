import pygame
import random
from cons import SIZE, X_STEP_INCREMENT, Y_STEP_INCREMENT


class Apple:
    """
        A class to represent the apple in the snake game

        ...

        Attributes
        ----------
        # TODO documentation of class Apple attributes, example below
        parent_screen : str
            first name of the person

        Methods
        -------
        # TODO documentation of class Apple methods, example below
        info(additional=""):
            Prints the person's name and age.
        """
    def __init__(self, parent_screen: pygame.Surface):
        """
        Initiates Apple object
        :param parent_screen: pygame.Surface object of parent screen
        """
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.x = SIZE * 3
        self.y = SIZE * 3

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(0, X_STEP_INCREMENT - 1) * SIZE
        self.y = random.randint(0, Y_STEP_INCREMENT - 1) * SIZE
