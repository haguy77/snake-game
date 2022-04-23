import pygame
from cons import SIZE

class Apple:
    """
        A class to represent the apple in the snake game

        ...

        Attributes
        ----------
        # TODO documentation of class Apple attributes, example below
        name : str
            first name of the person

        Methods
        -------
        # TODO ducomentation of class Apple methods, example below
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
