import pygame
import Colors
from Tileset import *

class TileMenu:

    def __init__(self, x_pos, y_pos, width, height):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        #Full Rect
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        pygame.font.init()
        self.tile_list = []
        self.newtile = Tileset(1, "images/tileset1.png", 0, 0)
        self.tile_list.append(self.newtile)
        self.selectedTile = 0
        self.selectionImage = pygame.image.load("images/selection.png")


    def getSelectedTile(self):
        return self.newtile.get_image().getsubsurface(20, 20, 20, 20)

    def update(self):
        print("Current location: {0} {1}".format(str(self.x_pos), str(self.y_pos)))

    def handle_keyevents(self, event):
        if (event.type == pygame.MOUSEBUTTONDOWN):
            x, y = event.pos
            if(self.rect.collidepoint(x, y)):
                crow = x / 32
                ccol = y / 32
                self.selectedTile = crow + (ccol * 5)

    def render(self, screen):
        for tile in self.tile_list:
            screen.blit(tile.get_image(), (tile.get_pos()))
        row = self.selectedTile % 5
        col = self.selectedTile / 5
        screen.blit(self.selectionImage, (row * 32, col * 32))


    def isSelected(self):
        return self.selected