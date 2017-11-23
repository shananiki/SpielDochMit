import sys, pygame
from MenuState import *

BLACK = 0, 0, 0
WHITE = 255, 255, 255


current_state = MenuState()

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("SpielDochMit - v0.0.0.1a")

print("Loaded Image")

clock = pygame.time.Clock()

box_x = 300
box_dir = 3

while 1:
    clock.tick(25)
    event = pygame.event.poll()

    #Mach screen neu !

    screen.fill(BLACK)
    current_state.handle_keyevents(event)
    current_state.update()
    current_state.render(screen)
    pygame.display.flip()