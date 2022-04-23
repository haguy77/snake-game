import pygame
import time
from pygame.locals import *
from snake import Snake
from apple import Apple
from cons import SIZE, GAME_HEIGHT, GAME_WIDTH


class Game:
    """
    A class to represent the snake game

    ...

    Attributes
    ----------
    # TODO documentation of class Game attributes, example below
    surface : str
        first name of the person

    Methods
    -------
    # TODO documentation of class Game methods, example below
    info(additional=""):
        Prints the person's name and age.
    """
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        self.surface.fill((110, 110, 5))
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    @staticmethod
    def _is_collision(x1: int, y1: int, x2: int, y2: int) -> bool:
        if x2 <= x1 < x2 + SIZE:
            if y2 <= y1 < y2 + SIZE:
                return True

    def _play(self):
        self.snake.walk()
        self.apple.draw()

        if self._is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()

                elif event.type == QUIT:
                    running = False
            self._play()
            time.sleep(0.2)
