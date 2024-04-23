# game.py
import numpy as np
import pygame
from settings import WIDTH, HEIGHT, BG_COLOR, NX_CELLS, NY_CELLS, DIM_CW, DIM_CH

class GameOfLife:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.screen.fill(BG_COLOR)
        self.game_state = np.zeros((NX_CELLS, NY_CELLS))
        self.new_game_state = np.zeros_like(self.game_state)
        self.pause = False
        self.initialize_patterns()
        self.speed = 0.07

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                elif event.key == pygame.K_r:
                    self.reset_board()
                elif event.key == pygame.K_t:
                    self.randomize_board()
                elif event.key == pygame.K_q:
                    self.speed -= 0.01
                    if self.speed < 0:
                        self.speed = 0.01

                elif event.key == pygame.K_w:
                    self.speed += 0.01
                elif event.key == pygame.K_SPACE:
                    self.pause = not self.pause

            mouse_click = pygame.mouse.get_pressed()
            if sum(mouse_click) > 0:
                self.handle_mouse(mouse_click)

    def handle_mouse(self, mouse_click):
        posX, posY = pygame.mouse.get_pos()
        celX, celY = int(posX / DIM_CW), int(posY / DIM_CH)
        self.new_game_state[celX, celY] = not mouse_click[2]

    def reset_board(self):
        self.new_game_state.fill(0)
        self.initialize_patterns()

    def randomize_board(self):
        self.new_game_state.fill(0)
        for _ in range(250):
            self.new_game_state[np.random.randint(NX_CELLS), np.random.randint(NY_CELLS)] = 1

    def initialize_patterns(self):
        # Configurar autómata en forma de palo
        self.new_game_state[5, 3] = 1
        self.new_game_state[5, 4] = 1
        self.new_game_state[5, 5] = 1

        # Configurar autómata móvil
        self.new_game_state[21, 21] = 1
        self.new_game_state[22, 22] = 1
        self.new_game_state[22, 23] = 1
        self.new_game_state[21, 23] = 1
        self.new_game_state[20, 23] = 1

    def update(self):
        self.screen.fill(BG_COLOR)
        for y in range(NX_CELLS):
            for x in range(NY_CELLS):
                if not self.pause:
                    self.update_cell(x, y)
                self.draw_cell(x, y)
        self.game_state = np.copy(self.new_game_state)

    def update_cell(self, x, y):
        n_neigh = self.count_neighbors(x, y)
        if self.game_state[x, y] == 0 and n_neigh == 3:
            self.new_game_state[x, y] = 1
        elif self.game_state[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
            self.new_game_state[x, y] = 0

    def count_neighbors(self, x, y):
        # Retorna el número de vecinos vivos
        return sum([self.game_state[(x + i) % NX_CELLS, (y + j) % NY_CELLS] for i in [-1, 0, 1] for j in [-1, 0, 1] if (i != 0 or j != 0)])

    def draw_cell(self, x, y):
        # Dibujar cada celda
        poly = [(x * DIM_CW, y * DIM_CH),
                ((x + 1) * DIM_CW, y * DIM_CH),
                ((x + 1) * DIM_CW, (y + 1) * DIM_CH),
                (x * DIM_CW, (y + 1) * DIM_CW)]
        if self.new_game_state[x, y] == 0:
            pygame.draw.polygon(self.screen, (128, 128, 128), poly, 1)
        else:
            pygame.draw.polygon(self.screen, (255, 255, 255), poly, 0)
