import pygame

class Button:
    image_path = 0
    x_pos = 0
    y_pos = 0
    width = 0
    height = 0
    image_surf = 0
    image_rect = 0

    def __init__(self, image_path, x_pos, y_pos, width, height, ID):
        self.image_path = image_path
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.ID = ID
        self.image_surf = pygame.image.load(image_path + ".png")
        self.image_surf_hover = pygame.image.load(image_path + "H.png")
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        self.hover = False

    def getID(self):
        return self.ID

    def setHover(self, value):
        self.hover = value

    def getHover(self):
        return self.hover

    def get_rect(self):
        return self.rect

    def get_x_pos(self):
        return self.x_pos

    def set_x_pos(self, new_x_pos):
        self.x_pos = new_x_pos

    def get_y_pos(self):
        return self.y_pos

    def set_y_pos(self, new_y_pos):
        self.y_pos = new_y_pos

    def get_image(self):
        if(self.hover):
            return self.image_surf_hover
        else:
            return self.image_surf
