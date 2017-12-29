import pygame
import Colors


class Interface:

    def __init__(self, x_pos, y_pos, width, height, topbar, ID, title):
        self.title = title
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.topbar = topbar
        self.ID = ID
        #Full Rect
        self.rect = pygame.Rect(self.x_pos, self.y_pos + 20, self.width, self.height - 20)
        #Topbar
        if(self.topbar):
            self.tRect = pygame.Rect(self.x_pos, self.y_pos, self.width, 20)
            self.xRect = pygame.Rect(self.x_pos + self.width - 20, self.y_pos, 20, 20)
        self.selected = False
        self.dragging = False
        self.visible = True
        pygame.font.init()

    def setVisible(self, value):
        self.visible = value

    def isVisible(self):
        return self.visible

    def getID(self):
        return self.ID

    def handle_basics(self, event):
        if (self.isVisible()):
            mouse_x, mouse_y = pygame.mouse.get_pos()
            rel_x, rel_y = pygame.mouse.get_rel()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if event.button == 1:
                    if (self.tRect.collidepoint(mouse_x, mouse_y)):
                        # Move by topbar
                        self.selected = True
                        self.dragging = True
                    else:
                        self.selected = False
                    if (self.xRect.collidepoint(mouse_x, mouse_y)):
                        self.visible = False
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.dragging = False
            elif (event.type == pygame.MOUSEMOTION):
                if (self.dragging):
                    self.tRect.x += rel_x
                    self.tRect.y += rel_y
                    self.rect.x += rel_x
                    self.rect.y += rel_y
                    self.xRect.x += rel_x
                    self.xRect.y += rel_y
                else:
                    self.dragging = False

    def getRect(self):
        return self.rect

    def handle_keyevents(self, event):
        self.handle_basics(event)

    def update(self):
        print("Current location: {0} {1}".format(str(self.x_pos), str(self.y_pos)))

    def renderMainWindow(self, screen):
        #Draw Background Rectangle
        pygame.draw.rect(screen, Colors.COLOR_GREYLIGHT, self.rect, 0)
        #Draw Top part of Interface
        if (self.topbar):
            pygame.draw.rect(screen, Colors.COLOR_GREYMD, (self.tRect.x, self.tRect.y, self.tRect.width - 20, self.tRect.height), 0)
            pygame.draw.rect(screen, Colors.COLOR_RED, self.xRect, 0)
            #Draw Title
            myfont = pygame.font.SysFont("monospace", 15)
            label = myfont.render(self.title, 1, Colors.COLOR_WHITE)
            screen.blit(label, (self.tRect.x + 2, self.tRect.y + 2))


    def render(self, screen):
        self.renderMainWindow(screen)

    def isSelected(self):
        return self.selected