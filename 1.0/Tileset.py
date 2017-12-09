import pygame
class Tileset:

    ID_0 = "None"
    ID_1 = "Grass"
    ID_2 = "Water"

    def __init__(self, ID, imgpath, x, y):
        self.ID = ID
        self.image = pygame.image.load(imgpath)
        self.x_pos = x
        self.y_pos = y

    def get_image(self):
        return self.image

    def get_pos(self):
        return self.x_pos, self.y_pos

    def get_Tile(self, ID):
        row = ID % 5
        col = ID / 5
        tilePos = (row, col)
        buff = pygame.Surface((32, 32), flags=0)
        buff.blit(self.image, (0, 0), area=tilePos)
        return buff


class Tile:

    def __init__(self, tile_ID):
        self.tile_ID = tile_ID
        self.image = 0

    def get_image(self, tile_ID):
        return self.image


