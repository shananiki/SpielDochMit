from GameState import *
from SelectionRectangle import *
from Inventory import Inventory
from Interface import Interface
from TileMenu import TileMenu
from Button import Button
from Menu import Menu
import pygame

class MapEditorState(GameState):

    def __init__(self):
        self.interface_list = []
        #inventory = Interface(120, 120, 180, 240, topbar=True)
        interfaceMenu = Menu(0, 0, 200, 40)
        self.interface_list.append(interfaceMenu)
        #self.interface_list.append(inventory)

        #self.b = Button("images/button.png", 22, 22, 20, 20)

    def render(self, screen):
        for interface in self.interface_list:
            if(interface.isVisible()):
                interface.render(screen)

    def handle_keyevents(self, event):
        for interface in self.interface_list:
            if(interface.isVisible()):
                interface.handle_keyevents(event)

    def update(self):
        if False == True:
            print("HELLO")
