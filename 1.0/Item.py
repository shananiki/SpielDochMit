import ItemDB
import pygame
class Item:

    def __init__(self, image_name):
        self.x_pos = 0
        self.y_pos = 0
        self.width = 0
        self.height = 0
        self.image_name = image_name
        self.image_surf = pygame.image.load(self.image_name)
        self.image_rect = 0


    def get_x_pos(self):
        return self.x_pos

    def get_y_pos(self):
        return self.y_pos

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_image(self):
        return self.image_surf

    def get_image_rect(self):
        return self.image_rect

    def set_x_pos(self, new_x_pos):
        self.x_pos = new_x_pos

    def set_y_pos(self, new_y_pos):
        self.y_pos = new_y_pos

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def set_image(self, new_image):
        self.image_surf = new_image

    def set_image_rect(self, new_image_rect):
        self.image_rect = new_image_rect
