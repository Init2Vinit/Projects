from constants import *

game_window = pygame.display.set_mode((window_width, window_height))

class Tiles(object):
    #constructor
    def __init__(self, row, col):
        self.location = row, col
        self.open = False
        self.mine = False
        self.flag = False
        self.neighbour_mine_count = 0

    def is_opened(self):
        return self.open #returns true if a tile is opened

    def open_tile(self):
        self.open = True #set to true boolean value

    def is_mine(self):
        return self.mine #returns true if a tile is a mine

    def set_mine(self, value: bool):
        self.mine = value #boolean value to check mine

    def is_flagged(self):
        return self.flag #returns true if a tile is flagged

    def set_flag(self, value: bool):
        self.flag = value #boolean value to check flag

    def get_location(self):
        return self.location #returns the tile's location

    def get_neighbour_mine_count(self):
        return self.neighbour_mine_count #returns the number of mines surrounding a tile

    def set_neighbour_mine_count(self, number: int):
        self.neighbour_mine_count = number #number of surrounding mines

    def draw_tile(self, window=game_window):
        #count for neighbouring mines -- used for numbered tiles
        count = self.get_neighbour_mine_count()

        #drawing the tiles on the window depending on the tile type
        if self.is_flagged():
            window.blit(image_dict["flag"], self.get_location())
        elif not self.is_opened():
            window.blit(image_dict["tile"], self.get_location())
        else:
            if self.is_mine():
                window.blit(image_dict["mine"], self.get_location())
            elif count > 0:
                window.blit(image_dict[str(count)], self.get_location())
            else:
                window.blit(image_dict["empty"], self.get_location())