import pygame
from gamestate import GameState


pygame.init()

game = GameState()

while True:
    game.handle_quit_and_pause_input()
    game.run()
