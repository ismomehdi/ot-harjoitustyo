import pygame
from game_state import GameState
from db.init_db import init_db

def main():
    pygame.init()

    game = GameState()

    while True:
        game.handle_user_input()
        game.run()

if __name__ == '__main__':
    main()
