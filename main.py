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
menu_text_font = pygame.font.Font(ARIAL_PATH, 36)

# Positions
main_menu_text_pos = list()

# Window, display and main screen
window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('TicTacDota')
screen = pygame.display.get_surface()
background = pygame.Surface(screen.get_size())

class MainMenu():
    """
    The main menu screen.
    """
    def draw(self):
        """
        Draw the main menu.
        """
        # Blit the surfaces one by one
        for text in self.text_surfaces:
            text_pos = text.get_rect(centerx = background.get_width() / 2,
                    centery = self.start_y + menu_text_font.get_height() + 8)
            # Store the position
            self.text_positions.append(text_pos)
            # Update the startY position
            self.start_y = self.start_y + menu_text_font.get_height() + 8
            # Blit the text
            screen.blit(text, text_pos)

    def __init__(self):
        # Initialize the list of text strings
        self.text_strings = ("Play against Timbersaw",
                "Play against Storm Spirit", "Play against yourself",
                "Exit")
        # Initialize the special positions
        self.menu_height = ((menu_text_font.get_height() + 8) *
                len(self.text_strings))
        self.start_y = background.get_height() / 2 - self.menu_height / 2
        self.text_positions = list()
        # Initialize the list of surfaces
        self.text_surfaces = list()
        for entry in self.text_strings:
            surface = menu_text_font.render(entry, 1, BLACK)
            self.text_surfaces.append(surface)

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

    # Start the background music
    pygame.mixer.init()
    #play_music(os.path.join(MUSIC_DIR, "monokuma.ogg"))

    # Initialize the sound used for clicks
    #click_sound = pygame.mixer.Sound(os.path.join("sound", "click.ogg"))
    # DEBUG: Print the sound path
    #print("Click sound loaded from: " + os.path.join("sound", "click.ogg"))

    # Start the main game loop
    while 1:
        # Check if we are in the main menu
        if current_game_screen == "main":
            # Initialize the game background
            bg_surface = pygame.image.load(os.path.join("images", 
                "bg_main.png"))
            # Blit the game background
            screen.blit(bg_surface, (0,0))
            # Create a main menu object
            main_menu = MainMenu()
            main_menu.draw()

        # Event handler
        for event in (pygame.event.get()):
            if event.type == QUIT:
                # User wants to quit
                sys.exit(0)
            elif event.type == MOUSEBUTTONDOWN:
                # Evaluate the mouse click
                # Get the position of the mouse click
                eventX = event.pos[0]
                eventY = event.pos[1]
                if current_game_screen == "main":
                    # We are in the main screen, evaluate main screen clicks
                    for pos in main_menu.text_positions:
                        if((eventX > pos.left and eventX < pos.right) and
                                (eventY > pos.top and eventY < pos.bottom)):
                            # DEBUG: Display a console message
                            print("Clicked " +
                                    main_menu.text_strings[main_menu.text_positions.
                                        index(pos)])
                            # Play a sound
                            #click_sound.play()
        
        # Update everything
        pygame.display.flip()

if __name__ == '__main__':
    main()
