from constants import *

class Fonts:
    #constructor
    def __init__(self, text, colour, bg_colour="black"):
        self.text = text
        self.colour = colours[colour]
        self.bg_colour = colours[bg_colour]
        self.text_size = font_size
        pygame.font.init()

    #getters and setters
    def get_colour(self):
        return self.colour #gets colour

    def get_text_size(self):
        return self.text_size #gets text size

    def set_colour(self, colour):
        self.colour = colours[colour] #set colours using colours dictionary from constants

    def set_bg_colour(self, colour):
        self.bg_colour = colours[colour] #set background colour using dictionary from constants

    def set_text(self, text):
        self.text = text #set some text

    def set_text_size(self, text_size):
        self.text_size = text_size #set text size

    def get_text_box(self):
        text = pygame.font.Font(font_type, self.get_text_size()) #generating fonts

        surface = text.render(self.text, True, self.colour, self.bg_colour) #text rendering on new surface
        return surface

    def display_text_box(self, window, x_pos, y_pos):
        text_box = self.get_text_box() #get text box

        text_width, text_height = text_box.get_size() #text box size

        if x_pos <0:
            text_position = x_pos + window_width - text_width, y_pos
        else:
            text_position = x_pos, y_pos #text box position

        window.blit(text_box, text_position) #draw the text box