#!/usr/bin/python

# Tic Tac Dota
#
#
#
# main.py
#
# The main Python file for the game. Run this to run the game.

# Import important modules
import os, random, pygame, sys
from pygame.locals import *

# Important constants
FPS = 30 # speed of the game
WINDOWWIDTH = 640 # width of the game window, in pixels
WINDOWHEIGHT = 480 # height of the game window, in pixels

# Directory constants
MUSIC_DIR = os.path.join("sounds", "music")

# Color constants (R,G,B)
GRAY = (100,100,100)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# Initialize Pygame and its window
pygame.init()
pygame.font.init()
title_text_font = pygame.font.Font(os.path.join(".", "arial.ttf"), 32)
window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('TicTacDota')
screen = pygame.display.get_surface()

def play_music(music_path):
    """
    Loads the music path passed as an argument and plays it.
    """
    # DEBUG: Display the music path
    print(music_path)

    # Play the background music
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play(-1)

def draw_timbersaw(pos_x, pos_y):
    """
    Draws timbersaw on the specified x and y coordinates.
    """
    # Load the timbersaw image
    timbersaw_path = os.path.join("images", "timbersaw.jpg")
    timbersaw_surface = pygame.image.load(timbersaw_path)

    # Blit the timbersaw surface into the screen
    screen.blit(timbersaw_surface, (pos_x, pos_y))

def main():
    """
    The main function.

    Most other function calls are called here.
    """
    print("Initializing TicTacDota...")

    # Start the background music
    pygame.mixer.init()
    play_music(os.path.join(MUSIC_DIR, "monokuma.ogg"))

    # Start the main game loop
    while 1:
        # DEBUG: Draw the face of timbersaw
        draw_timbersaw(0, 0)
        # DEBUG: Draw some text
        text_surface = title_text_font.render("I'm Timbersaw!", 0, RED)
        screen.blit(text_surface, (320, 20))

        # Event handler
        for event in (pygame.event.get()):
            if event.type == QUIT:
                # User wants to quit
                sys.exit(0)
        
        # Update everything
        pygame.display.flip()

if __name__ == '__main__':
    main()
