from GameState import *
from SelectionRectangle import *
from Inventory import Inventory
from Interface import Interface
import pygame
class CharacterSelectState(GameState):

    def __init__(self):
        self.interface_list = []

    def render(self, screen):
        for interface in self.interface_list:
            screen.blit(interface.get_image(), (interface.get_x_pos(), interface.get_y_pos()))

