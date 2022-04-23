import pygame


class Snake:
    def __init__(self, parent_screen: pygame.Surface):
        """
        Initiates Snake object
        :param parent_screen: pygame.Surface object of parent screen
        """
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = 100
        self.y = 100
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
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()

    def walk(self):
        if self.direction == "up":
            self.y = self.y - 10
        if self.direction == "down":
            self.y = self.y + 10
        if self.direction == "left":
            self.x = self.x - 10
        if self.direction == "right":
            self.x = self.x + 10

        self.draw()
