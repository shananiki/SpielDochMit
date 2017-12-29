from Interface import Interface
import pygame




class Inventory(Interface):


    def __init__(self, x_pos, y_pos, width, height, topbar, ID):
        Interface.__init__(self, x_pos, y_pos, width, height, topbar, ID, "Inventory")
        self.inventorySpots = []
        for x in range(10):
            self.inventorySpots.append(InventorySpot())

    def render(self, screen):
        self.renderMainWindow(screen)
        self.renderInventory(screen)

    def renderInventory(self, screen):
        spacing = 32
        count = 0
        for spot in self.inventorySpots:
            rows = count / 5
            cols = count % 5
            screen.blit(spot.get_image(), (self.rect.x + 2 + (count * 32), self.rect.y + 2))
            count += 1


    def handle_keyevents(self, event):
        self.handle_basics(event)

class InventorySpot:
    inventorySpotIMG = pygame.image.load("images/inventorySpot.png")

    def get_image(self):
        return self.inventorySpotIMG

    def get_x_pos(self):
        return self.x_pos

    def get_y_pos(self):
        return self.y_pos



