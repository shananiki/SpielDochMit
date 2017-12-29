from Interface import Interface
import pygame

class Skilltree(Interface):


    def __init__(self, x_pos, y_pos, width, height, topbar, ID):
        Interface.__init__(self, x_pos, y_pos, width, height, topbar, ID, "Skilltree")
        self.panel = Skilltreepanel(20, 20)

    def render(self, screen):
        self.renderMainWindow(screen)
        self.renderSkillTree(screen)

    def handle_keyevents(self, event):
        self.handle_basics(event)

    def renderSkillTree(self, screen):
        if (True == False):
            print("HELLO")



from Panel import Panel
import Colors
class Skilltreepanel(Panel):

    def __init__(self, x_pos, y_pos):
        Panel.__init__(self, x_pos, y_pos)



    def render(self, screen, x, y):
        pygame.draw.rect(screen, Colors.COLOR_RED, (x, y, 32, 32), 0)