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

    def draw(self):
        self.parent_screen.fill((110, 110, 5))
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()

    def move_left(self):
        self.x = self.x - 10
        self.draw()

    def move_right(self):
        self.x = self.x + 10
        self.draw()

    def move_up(self):
        self.y = self.y - 10
        self.draw()

    def move_down(self):
        self.y = self.y + 10
        self.draw()
