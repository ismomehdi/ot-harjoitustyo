import pygame
from config.display import display_surface


def draw_text(text, font, size, color, position):
    """Draws text on the display surface.

    Args:
        text: The text to be drawn.
        font: The font of the text.
        size: The size of the text.
        color: The color of the text.
        position: The position of the text.
    """

    font = pygame.font.Font(font, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = position
    display_surface.blit(text_surface, text_rect)
