import pygame
from game_state import GameState

def main():
    pygame.init()

    game = GameState()

    while True:
        game.handle_quit_and_pause_input()
        game.run()

if __name__ == '__main__':
    main()