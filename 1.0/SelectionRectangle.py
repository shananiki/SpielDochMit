import pygame
class SelectionRectangle:

    BLUE = (0, 255, 255)

    def __init__(self):
        self.starting_pos = (0, 0)
        self.width = 0
        self.height = 0
        self.end_pos = (0, 0)

    def setStartPos(self, pos):
        print("Set Start Pos" + str(pos))
        self.starting_pos = pos

    def setEndPos(self, pos):
        print("Set End Pos" + str(pos))
        self.end_pos = (pos[0] - self.starting_pos[0], pos[1] - self.starting_pos[1])

    def handle_events(self, event):
        print("Hello")


    def update(self):
        print("update SENDER MENUSTATE")

    def getRectangle(self):
        return pygame.Rect(self.starting_pos[0], self.starting_pos[1], self.end_pos[0], self.end_pos[1])

    def render(self, screen):
        pygame.draw.rect(screen, (0, 255, 255), self.getRectangle(), 0)


