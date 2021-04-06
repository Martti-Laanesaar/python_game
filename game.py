import sys
import pygame

def run_game():
    # init game and create display object
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("PyGame")

    while True:
        # control keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # display the last screen
        pygame.display.flip()
# test game
run_game()