from GameState import *
from SelectionRectangle import *
from Inventory import Inventory
import pygame
class MenuState(GameState):

    def __init__(self):
        self.rect = pygame.Rect(5, 5, 5, 5)
        self.isMouseDown = False
        self.selection = SelectionRectangle()
        self.inventory = Inventory(0, 100, 200, 200, "Inventar")

    def handle_keyevents(self, event):
        if(self.isMouseDown == False):
            if (event.type == pygame.MOUSEBUTTONDOWN):
                self.isMouseDown = True
                self.selection.setStartPos(event.pos)
                self.selection.setEndPos(event.pos)

        elif(self.isMouseDown == True):
            if(event.type == pygame.MOUSEMOTION):
                self.selection.setEndPos(event.pos)
            elif(event.type == pygame.MOUSEBUTTONUP):
                self.isMouseDown = False
                self.selection.setEndPos(event.pos)
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                self.selection.setStartPos(event.pos)

    def update(self):
        print("Selection Rect: " + str(self.selection.getRectangle()))

    def render(self, screen):
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render("Mouse is: NOT DOWN", 1, (255, 255, 0))
        if(self.isMouseDown == True):
            self.selection.render(screen)
            label = myfont.render("Mouse is: DOWN", 1, (255, 255, 0))
        screen.blit(label, (10, 10))
        self.inventory.render(screen)

