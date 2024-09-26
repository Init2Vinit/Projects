from constants import *
from texts import Fonts

class Button(object):
    #constructor
    def __init__(self, colour, x, y, width=button_width, height=button_height, text=None):
        self.colour = colours[colour]
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    #getters and setters
    def get_colour(self):
        return self.colour

    def set_colour(self, colour):
        self.colour = colours[colour]

    def set_text(self, text):
        self.text = text

    def get_button_rect(self):
        return pygame.Rect((self.x, self.y), (self.width, self.height))

    #drawing the button on the window
    def draw_button(self, window):

        text = Fonts(self.text, colour="black", bg_colour="white")
        text_box = text.get_text_box()

        x, y = self.get_button_rect().center
        x_pos = x - text_box.get_width() // 2
        y_pos = y - text_box.get_height() // 2

        pygame.draw.rect(window, self.get_colour(), self.get_button_rect())
        text.display_text_box(window, x_pos, y_pos)