#pragma once
import pygame
import Colors
class Inventory:

    rows = 2
    columns = 2

    def __init__(self, x_pos, y_pos, width, height, name):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.inventoryspots = []
        self.spots = 0
        self.name = name
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        self.icon = pygame.image.load('images/inventory.png')
        pygame.font.init()
        self.myfont = pygame.font.SysFont("monospace", 15)


    def render(self, screen):
        #Draw Background Rectangle
        pygame.draw.rect(screen, Colors.COLOR_GREYLIGHT, self.rect, 0)
        #Write Inventarname to Top of Inventar Rectangle
        label = self.myfont.render(self.name, 1, (255, 255, 255))
        screen.blit(label, (self.x_pos + 10,  self.y_pos + 3))

        #Blit Icon to Screen
        #screen.blit(self.icon, (self.x_pos + 2, self.y_pos + 2))

        #Draw X to the top right
        pygame.draw.rect(screen, Colors.COLOR_RED, (self.x_pos + self.width - 20, self.y_pos, 20, 20), 0)
        #Draw Inventory Spots on X = 0
        for x in range(4):
            spotrect = pygame.Rect(self.x_pos + 4, self.y_pos + 30 + x*36, 32, 32)
            pygame.draw.rect(screen, Colors.COLOR_GREYDIM, spotrect, 0)

        #Draw Inventory Spots on X = 1
        for x in range(4):
            spotrect = pygame.Rect(self.x_pos + 40, self.y_pos + 30 + x*36, 32, 32)
            pygame.draw.rect(screen, Colors.COLOR_GREYDIM, spotrect, 0)


class InventorySpot:
    def __init__(self, x_pos, y_pos, width, height):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height