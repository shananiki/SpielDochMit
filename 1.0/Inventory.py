from Interface import Interface
import pygame

class Inventory(Interface):


    def __init__(self, x_pos, y_pos, width, height, topbar, ID):
        Interface.__init__(self, x_pos, y_pos, width, height, topbar, ID)

    def render(self, screen):
        self.renderMainWindow(screen)

    def handle_keyevents(self, event):
        self.handle_basics(event)