import pygame
import time
from pygame.locals import *
from snake import Snake
from apple import Apple
from cons import *


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
        pygame.display.set_caption("Snake And Apple Game")

        pygame.mixer.init()
        self._play_background_music()

        self.surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        self.render_background()
        self.snake = Snake(self.surface, SNAKE_INITIAL_SIZE)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    @staticmethod
    def _is_collision(x1: int, y1: int, x2: int, y2: int) -> bool:
        if x2 <= x1 < x2 + SIZE:
            if y2 <= y1 < y2 + SIZE:
                return True
        return False

    @staticmethod
    def _play_background_music():
        pygame.mixer.music.load("resources/bg_music_1.mp3")
        pygame.mixer.music.play()

    @staticmethod
    def _play_sound(sound):
        sound = pygame.mixer.Sound(f"resources/{sound}.mp3")
        pygame.mixer.Sound.play(sound)

    def render_background(self):
        bg = pygame.image.load("resources/background.jpg")
        self.surface.blit(bg, (0, 0))

    def _play(self):
        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        # Snake colliding with apple
        if self._is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self._play_sound("ding")
            self.snake.increase_length()
            self.apple.move()

        # Snake colliding with itself
        for i in range(3, self.snake.length):
            if self._is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self._play_sound("crash")
                raise Exception("Game Over")

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length - SNAKE_INITIAL_SIZE}", True, SCORE_FONT_COLOR)
        self.surface.blit(score, (SCORE_X, SCORE_Y))

    def show_game_over(self):
        self.render_background()
        font = pygame.font.SysFont('arial', GAME_OVER_FONT_SIZE)
        line1 = font.render(f"Game is over ! Your score is {self.snake.length - SNAKE_INITIAL_SIZE}", True, SCORE_FONT_COLOR)
        self.surface.blit(line1, GAME_OVER_XY)
        line2 = font.render("To play again press ENTER, To exit press ESCAPE !", True, SCORE_FONT_COLOR)
        self.surface.blit(line2, PLAY_AGAIN_XY)

        pygame.display.flip()

        pygame.mixer.music.pause()

    def reset(self):
        self.snake = Snake(self.surface, SNAKE_INITIAL_SIZE)
        self.apple = Apple(self.surface)

    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False
                    if not pause:
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
            try:
                if not pause:
                    self._play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()
            time.sleep(0.2)

# TODO Add out of screen feature to come back from different side
# TODO Add increase speed feature when snake getting bigger
# TODO Export game to .EXE file
