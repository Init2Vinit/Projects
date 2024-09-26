import pygame

#game window
window_width = 800
window_height = 640

#font
font_size = 30
font_type = "fonts/Virtucorp.otf"

#extra constants for design and style
text_padding = 5
tile_size = 32
button_width = 160
button_height = 32

#colours dictionary
colours = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255,),
    "yellow": (255, 255, 0),
    "cyan": (0, 255, 255),
    "purple": (255, 0, 255),
    "crimson": (220, 20, 60),
}

#dictionary for tiles
image_dict = dict()

#tiles without numbers
image_dict["tile"] = pygame.image.load("images/tiles.png")
image_dict["empty"] = pygame.image.load("images/blank.jpg")
image_dict["flag"] = pygame.image.load("images/flag.png")
image_dict["mine"] = pygame.image.load("images/bomb.png")

#number tiles
for i in range(1, 9):
    image_dict[str(i)] = pygame.image.load(f"images/{i}.png")