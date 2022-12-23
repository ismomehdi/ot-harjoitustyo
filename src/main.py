import pygame
from game_state import GameState
from db.config import setup_database

def main():
    pygame.init()

    game = GameState()

    while True:
        game.handle_user_input()
        game.run()

if __name__ == '__main__':
    setup_database()
    main()
