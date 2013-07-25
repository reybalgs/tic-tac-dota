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

# Import game modules
from ai_timbersaw import *
from tictactoe_game import *

# Important constants
FPS = 30 # speed of the game
WINDOWWIDTH = 640 # width of the game window, in pixels
WINDOWHEIGHT = 480 # height of the game window, in pixels

# Directory and path constants
MUSIC_DIR = os.path.join("sounds", "music")
ARIAL_PATH = os.path.join(".", "arial.ttf")

# Color constants (R,G,B)
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (100,100,100)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# Initialize Pygame and its window
pygame.init()
pygame.font.init()

# Important global variables
# Fonts
title_text_font = pygame.font.Font(ARIAL_PATH, 40)
menu_text_font = pygame.font.Font(ARIAL_PATH, 28)

# Window, display and main screen
window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('TicTacDota')
screen = pygame.display.get_surface()

class MainMenu():
    """
    The main menu screen.
    """
    def draw(self):
        """
        Draw the main menu.
        """
        # Blit the title text surface into the screen
        screen.blit(self.title_text_surface, (200, 60))
        # Blit all the other text surfaces onto the screen
        screen.blit(self.play_timbersaw_surface, (150, 180))
        screen.blit(self.play_stormspirit_surface, (150, 240))
        screen.blit(self.play_self_surface, (150, 300))
        screen.blit(self.exit_text_surface, (150, 360))

    def __init__(self):
        # Initialize the title text surface
        self.title_text_surface = title_text_font.render("TicTacDota", 1,
            BLACK)
        # Initialize all the other text surfaces
        self.play_timbersaw_surface = menu_text_font.render("Play against" +
            " Timbersaw", True, BLACK)
        self.play_stormspirit_surface = menu_text_font.render("Play against" +
            " Storm Spirit", True, BLACK)
        self.play_self_surface = menu_text_font.render("Play against yourself",
            True, BLACK)
        self.exit_text_surface = menu_text_font.render("Exit", True, BLACK)

def play_music(music_path):
    """
    Loads the music path passed as an argument and plays it.
    """
    # DEBUG: Display the music path
    print("Loaded music: " + music_path)

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

    # Create a variable to check which game screen we are in. It is initially
    # set to the main menu.
    current_game_screen = "main"

    # Initialize the game background
    bg_surface = pygame.image.load(os.path.join("images", "bg_main.png"))
    # Blit the game background
    screen.blit(bg_surface, (0,0))

    # Start the background music
    pygame.mixer.init()
    play_music(os.path.join(MUSIC_DIR, "monokuma.ogg"))

    # Start the main game loop
    while 1:
        # Check if we are in the main menu
        if current_game_screen == "main":
            # Create a main menu object
            main_menu = MainMenu()
            main_menu.draw()

        # Event handler
        for event in (pygame.event.get()):
            if event.type == QUIT:
                # User wants to quit
                sys.exit(0)
        
        # Update everything
        pygame.display.flip()

if __name__ == '__main__':
    main()
