import pygame


def player_input(direction, jump_speed, player_on_ground, keys):
    """Controls the player movement based on the key input."""
    if keys[pygame.K_RIGHT]:
        direction.x = 1
    elif keys[pygame.K_LEFT]:
        direction.x = -1
    else:
        direction.x = 0

    if keys[pygame.K_UP] and player_on_ground:
        direction.y = -jump_speed
