import pygame
from Button import Button
import Colors
from Interface import Interface
from Inventory import Inventory
class Menu:


    def __init__(self, x_pos, y_pos, width, height):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        self.visible = True
        self.buttonList = []
        helmetButton = Button("images/helmet", self.x_pos + 2, self.y_pos, 32, 32, ID=1)
        inventoryButton = Button("images/inventory", self.x_pos + 36, self.y_pos, 32, 32, ID=2)
        skilltreeButton = Button("images/skilltree", self.x_pos + 70, self.y_pos, 32, 32, ID=3)
        self.buttonList.append(helmetButton)
        self.buttonList.append(inventoryButton)

        #Test
        inventory = Inventory(120, 120, 180, 240, True, ID=2)
        self.interface_list = []
        self.interface_list.append(inventory)


    def setVisible(self, value):
        self.visible = value

    def isVisible(self):
        return self.visible

    def renderBackground(self, screen):
        pygame.draw.rect(screen, Colors.COLOR_GREYMD, self.rect, 0)

    def renderButton(self, screen):
        for button in self.buttonList:
            screen.blit(button.get_image(), (button.get_x_pos(), button.get_y_pos() + 2))

    def render(self, screen):
        self.renderBackground(screen)
        self.renderButton(screen)
        for interface in self.interface_list:
            if(interface.isVisible()):
                interface.render(screen)

    def handle_keyevents(self, event):
        for interface in self.interface_list:
            interface.handle_keyevents(event)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for button in self.buttonList:
            if (event.type == pygame.MOUSEMOTION):
                if(button.get_rect().collidepoint(mouse_x, mouse_y)):
                    button.setHover(True)
                else:
                    button.setHover(False)
            elif(event.type == pygame.MOUSEBUTTONDOWN):
                if event.button == 1:
                    if (button.get_rect().collidepoint(mouse_x, mouse_y)):
                        buttonID = button.getID()
                        for interface in self.interface_list:
                            if(interface.getID() == buttonID):
                                if interface.isVisible() == False:
                                    interface.setVisible(True)
                                else:
                                    interface.setVisible(False)


    def update(self):
        if(True == False):
            print("HELLO")
