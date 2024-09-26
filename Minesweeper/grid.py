import random
from constants import tile_size
from tile import Tiles

class Grid(object):
    #constructor
    def __init__(self, x, y, grid_size, mines):
        self.x = x
        self.y = y
        self.N = grid_size
        self.mines_num = mines
        self.mines_count = mines
        self.grid_dict = dict()
        self.mines_dict = dict()

        #generate the grid when the new instance is made
        self.generate_grid(self.N, self.mines_num)

    #getters and setters
    def get_grid_dict(self):
        return self.grid_dict.copy()

    def get_grid_size(self):
        return self.N

    def get_mine_count(self):
        return self.mines_count

    def set_mine_count(self, mines_count):
        self.mines_count = mines_count

    def get_mines_dict(self):
        return self.mines_dict.copy()

    def get_neighbour_tiles(self, row, col):
        #current cell is (x, y) there are total 8 neighbours
        #top:(x, y - 1), top-left:(x - 1, y - 1) , top-right:(x + 1, y - 1)
        #left:(x - 1, y), right:(x + 1, y)
        #bottom:(x, y + 1), bottom-left: (x - 1, y + 1), bottom-right: (x + 1, y + 1)
        #all those neighbours can be achieved by adding (-1, 0 or 1) to (x, y)
        #2 positions (x, y), 3 possible choices (-1, 0, 1) => 2^3 = 8 neighbours

        #to store neighbours (index) -> tile
        neighbours = dict()

        #bounds of grid for indexing
        lo, hi = 0, self.get_grid_size()

        #iterate through all neighbours
        for i in range(-1, 2):
            for j in range(-1, 2):
                #check for this neighbours
                check_row, check_col = row + i, col + j

                if lo <= check_row < hi and lo <= check_col < hi:
                    neighbour_tile = self.get_grid_dict()[(row + i, col + j)]
                    neighbours[(check_row, check_col)] = neighbour_tile

        #return a copy to prevent accidental modifications
        return neighbours.copy()

    #generate the grid
    def generate_grid(self, n, m):
        #total size of grid must be greater than number of mines
        assert (n * n) > m #m < nxn --> n = grid size, m = number of mines

        #generate different type of tiles
        self.generate_tiles(n)
        self.generate_mines()
        self.generate_numbered_tiles()

    #generate the tiles
    def generate_tiles(self, n):
        y_pos = self.y

        #iterate through each row
        for row in range(n):
            x_pos = self.x

            #iterate through each column in the row
            for col in range(n):
                tile = Tiles(x_pos, y_pos)
                self.grid_dict[(row, col)] = tile
                x_pos += tile_size
            y_pos += tile_size

    #generate the mines
    def generate_mines(self):
        #mine counter
        count = 0

        #generate mines_num mine at random places in grid
        while count != self.mines_num:

            #select a random location for mine in the grid
            location = random.choice(list(self.get_grid_dict()))

            #check for location is already a mine, if so do nothing
            if location in self.get_mines_dict():
                continue

            #set a mine on this location in the grid
            mine = self.get_grid_dict()[location]
            count += 1
            mine.set_mine(True)
            self.mines_dict[location] = mine

    #generate numbered tiles
    def generate_numbered_tiles(self):
        def mine_counter(check_tile):
            return 1 if check_tile.is_mine() else 0 #checking if the tile is a mine or not

        #iterate over grid
        for row, col in self.get_grid_dict():
            #for each tile count neighbours mines
            counter = 0

            #if this grid location is a mine, do nothing
            if self.get_grid_dict()[(row, col)].is_mine():
                continue

            #iterate over neighbours to count number of surrounding mines
            for tile in self.get_neighbour_tiles(row, col).values():
                counter += mine_counter(tile)

            #set a number to this tile, number is same as surrounding mines
            tile = self.get_grid_dict()[(row, col)]
            tile.set_neighbour_mine_count(counter)

    #convert a grid location to tile index
    def convert_grid_location_to_tile_index(self, x, y):
        #iterate over grid
        for tile_index, tile in self.get_grid_dict().items():
            tile_x, tile_y = tile.get_location()
            #if location somewhere inside a tile area, use that tile index
            if tile_x <= x <= tile_x + tile_size:
                    if tile_y <= y <= tile_y + tile_size:
                        return tile_index

        #return out of bound index for mouse click outside grid
        return -1, -1

    #draw all tiles of grid
    def draw_grid(self):
        #iterate over tiles in the grid
        for tile in self.get_grid_dict().values():
            tile.draw_tile()

    #update the tile within the grid according to different clicks of mouse
    def update(self, x, y, click):
        #bounds for indexing
        lo, hi = 0, self.get_grid_size()

        #update if mouse click is within grid area
        try:
            tile_index = self.convert_grid_location_to_tile_index(x, y)
            assert (lo, lo) <= tile_index < (hi, hi)

        except AssertionError:
            #when mouse is clicked outside of the grid boundary
            pass

        else:
            #mouse click is within the grid now
            tile = self.get_grid_dict()[tile_index]
            flagged = tile.is_flagged()

            if click == "right":
                #proceed only if tile is not opened
                if not tile.is_opened():
                    if flagged:
                        self.set_mine_count(self.get_mine_count() + 1)
                    else:
                        self.set_mine_count(self.get_mine_count() - 1)
                    #toggle the flag status
                    tile.set_flag(not flagged)
                    tile.draw_tile()

            elif click == "left":
                #proceed only if tile is not opened
                if not tile.is_opened() and not tile.is_flagged():
                    if tile.is_mine():
                        return self.check_lost()
                    self.show_tile(tile_index[0], tile_index[1])
                    return self.check_won()

    #show the tile
    def show_tile(self, row, col):
        #drawing the tiles
        tile = self.get_grid_dict()[(row, col)]
        tile.open_tile()
        tile.draw_tile()

        #if tile is empty, open neighbours recursively
        if tile.get_neighbour_mine_count() == 0:
            self.show_neighbours(row, col)

    #show neighbouring tiles
    def show_neighbours(self, row, col):
        #open the tile only if
        #1. it's not open already and
        #2. it's not a mine and
        #3. it's not flagged
        for tile_index, tile in self.get_neighbour_tiles(row, col).items():
            if not (tile.is_mine() or tile.is_opened() or tile.is_flagged()):
                self.show_tile(tile_index[0], tile_index[1])

    #check if the game is won
    def check_won(self):
        #game is won when all tiles that are not mines, are opened
        count = sum(1 if tile.is_opened() and not tile.is_mine() else 0
                    for tile in self.get_grid_dict().values())

        #if count matches the actual non-mine opened tiles, game is won
        if count == self.N ** 2 - self.mines_num:
            #turn mines into flags
            for tile in self.get_grid_dict().values():
                tile.open_tile()
                if tile.is_mine():
                    tile.set_flag(True)

            #draw the full grid
            #self.set_mine_count(0)
            self.draw_grid()
            return "won"

    #check if the game is lost
    def check_lost(self):
        #draw all mines
        for tile in self.get_grid_dict().values():
            tile.open_tile()
            tile.set_flag(False)
        
        #draw the full grid
        self.draw_grid()
        return "lost"