import pygame
from pygame import locals


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((500, 400), 0, 32)
        self.clock = pygame.time.Clock()

        self.BLUE = (0, 0, 255)
        self.WHITE = (255, 255, 255)

        self.screen.fill(self.WHITE)
        self.snake = pygame.draw.rect(self.screen, self.BLUE, (20, 20, 20, 20))
        self._move = 't'

    def draw(self):
        self.snake = pygame.draw.rect(self.screen, (0, 0, 128), self.snake)

    @property
    def move(self):
        return self._move

    @move.setter
    def move(self, value):
        if value in ('t', 'b', 'r', 'l'):
            self._move = value
        raise ValueError('The move value must be equal "t" or "b" or "r" or "l"')

    def move_on(self,move):
        if move == 't':
            pass
        elif move == 'b':
            pass
        elif move == 'b':
            pass
        elif move == 'b':
            pass

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.screen.fill((255, 255, 255))
            self.draw()
            self.key_handler()
            pygame.display.update()

            self.clock.tick(50)

    def key_handler(self, move=5):
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT] and self.snake.left != 0:
            self.snake.move_ip(-move, 0)
        elif key[pygame.K_RIGHT] and self.snake.left != (self.screen.get_width() - self.snake.width):
            self.snake.move_ip(move, 0)
        elif key[pygame.K_UP] and self.snake.top != 0:
            self.snake.move_ip(0, -move)
        elif key[pygame.K_DOWN] and self.snake.top != (self.screen.get_height() - self.snake.height):
            self.snake.move_ip(0, move)


if __name__ == "__main__":
    game = Game()
    game.start()
