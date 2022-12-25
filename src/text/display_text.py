from services.draw_text import draw_text

class DisplayText:
    def __init__(self):
        """The DisplayText class is used for all the text drawn on the screen.
        """
        pass

    def score(self, score):
        """Draws the score on the screen.
        """

        text = f'SCORE: {score:04}'
        font = 'src/assets/fonts/Broken Console Bold.ttf'
        size = 30
        color = '#735d78'
        position = (1150, 30)

        draw_text(text, font, size, color, position)
