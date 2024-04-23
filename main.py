# main.py
import time
import pygame
from game import GameOfLife

def main():
    pygame.init()
    game = GameOfLife()

    while True:
        time.sleep(game.speed)
        game.handle_events()
        game.update()
        pygame.display.flip()

if __name__ == "__main__":
    main()