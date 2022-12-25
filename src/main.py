import pygame
from game_state import GameState
from db.config import setup_database

def main():
    """Main function of the game. Initializes the game and runs it.
    """
    pygame.init()
    game = GameState()

    while True:
        game.handle_user_input()
        game.run()

if __name__ == '__main__':
    setup_database()
    main()
