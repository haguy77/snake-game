import pygame
from cons import SIZE


class Snake:
    """
        A class to represent the snake in the snake game

        ...

        Attributes
        ----------
        # TODO documentation of class Snake attributes, example below
        name : str
            first name of the person

        Methods
        -------
        # TODO ducomentation of class Snake methods, example below
        info(additional=""):
            Prints the person's name and age.
        """
    def __init__(self, parent_screen: pygame.Surface, length):
        """
        Initiates Snake object
        :param parent_screen: pygame.Surface object of parent screen
        :param length: initial length of snake
        """
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = [SIZE] * length
        self.y = [SIZE] * length
        self.direction = "down"

    def move_left(self):
        self.direction = "left"

    def move_right(self):
        self.direction = "right"

    def move_up(self):
        self.direction = "up"

    def move_down(self):
        self.direction = "down"

    def draw(self):
        self.parent_screen.fill((110, 110, 5))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def walk(self):

        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == "up":
            self.y[0] = self.y[0] - SIZE
        if self.direction == "down":
            self.y[0] = self.y[0] + SIZE
        if self.direction == "left":
            self.x[0] = self.x[0] - SIZE
        if self.direction == "right":
            self.x[0] = self.x[0] + SIZE

        self.draw()
