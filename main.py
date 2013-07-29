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
from ai_stormspirit import *
from tictactoe_game import *

# Important constants
FPS = 25 # speed of the game
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

# A game clock
clock = pygame.time.Clock()

# Important global variables
# Fonts
menu_text_font = pygame.font.Font(ARIAL_PATH, 36)
name_text_font = pygame.font.Font(ARIAL_PATH, 28)
score_text_font = pygame.font.Font(ARIAL_PATH, 60)

# Positions
main_menu_text_pos = list()
grid_start = (160, 40)
quit_rect = Rect(520,10,80,60)
# Generate grid rects
location_rects = list()
location_names = ['topleft', 'topcenter', 'topright', 'middleleft',
'middlecenter', 'middleright', 'bottomleft', 'bottomcenter', 'bottomright']
location_rects.append(pygame.Rect(160, 40, 100, 100))
location_rects.append(pygame.Rect(260, 40, 100, 100))
location_rects.append(pygame.Rect(360, 40, 100, 100))
location_rects.append(pygame.Rect(160, 140, 100, 100))
location_rects.append(pygame.Rect(260, 140, 100, 100))
location_rects.append(pygame.Rect(360, 140, 100, 100))
location_rects.append(pygame.Rect(160, 240, 100, 100))
location_rects.append(pygame.Rect(260, 240, 100, 100))
location_rects.append(pygame.Rect(360, 240, 100, 100))

# Window, display and main screen
window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('TicTacDota')
screen = pygame.display.get_surface()
background = pygame.Surface(screen.get_size())

class GameScreen():
    """
    Class defining the visual logic of the tictactoe game. All the game logic
    is defined in the tictactoe_game.py file, in the TicTacToe() class.
    """

    def draw(self, game):
        """
        Draws the game board. Takes data from the TicTacToe game class.
        """
        # A variable to track which location we are in.
        location = 1

        # Draw the background image
        screen.blit(self.bg_image, (0,0))
        # Draw the player's portrait image
        screen.blit(self.player_portrait, (0,(480 - 130)))
        # Draw the opponent's portrait image
        screen.blit(self.opponent_portrait, ((640 - 110),(480 - 130)))
        # Draw the player's name text
        screen.blit(self.player_name, (120, (480 - 130)))
        # Draw the opponent's name text
        screen.blit(self.opponent_name, (360, (480 - 130)))
        # Draw the player's score text
        screen.blit(self.player_score, (120, (480 - 80)))
        # Draw the opponent's score text
        screen.blit(self.opponent_score, (420, (480 - 80)))
        # Draw the quit text
        screen.blit(self.quit, (520, 10))
        # Draw the marks on the game board.
        if game.board['topleft'] == 'x':
            screen.blit(self.mark_x, (170,50))
        elif game.board['topleft'] == 'o':
            screen.blit(self.mark_o, (170,50))
        if game.board['topcenter'] == 'x':
            screen.blit(self.mark_x, (270,50))
        elif game.board['topcenter'] == 'o':
            screen.blit(self.mark_o, (270,50))
        if game.board['topright'] == 'x':
            screen.blit(self.mark_x, (370,50))
        elif game.board['topright'] == 'o':
            screen.blit(self.mark_o, (370,50))
        if game.board['middleleft'] == 'x':
            screen.blit(self.mark_x, (170,150))
        elif game.board['middleleft'] == 'o':
            screen.blit(self.mark_o, (170,150))
        if game.board['middlecenter'] == 'x':
            screen.blit(self.mark_x, (270,150))
        elif game.board['middlecenter'] == 'o':
            screen.blit(self.mark_o, (270,150))
        if game.board['middleright'] == 'x':
            screen.blit(self.mark_x, (370,150))
        elif game.board['middleright'] == 'o':
            screen.blit(self.mark_o, (370,150))
        if game.board['bottomleft'] == 'x':
            screen.blit(self.mark_x, (170,250))
        elif game.board['bottomleft'] == 'o':
            screen.blit(self.mark_o, (170,250))
        if game.board['bottomcenter'] == 'x':
            screen.blit(self.mark_x, (270,250))
        elif game.board['bottomcenter'] == 'o':
            screen.blit(self.mark_o, (270,250))
        if game.board['bottomright'] == 'x':
            screen.blit(self.mark_x, (370,250))
        elif game.board['bottomright'] == 'o':
            screen.blit(self.mark_o, (370,250))
        # Display winning messages, if any
        if game.check_winner('o'):
            #screen.blit(self.player_lose, (5, 5))
            screen.blit(self.player_win, (5, 5))
        if game.check_winner('x'):
            screen.blit(self.player_lose, (5, 5))
            #screen.blit(self.player_win, (5, 5))

    def __init__(self, opponent, game):
        """
        Initialization function.

        Arguments:
        opponent = string that states the opponent of the player. Can either
        be "timbersaw", "storm_spirit" or "self".
        game = a TicTacToe() object, containing the game logic.
        """
        # Initialize the background image
        self.bg_image = pygame.image.load(os.path.join("images",
            "bg_game.png"))
        # Initialize the player's portrait image
        self.player_portrait = pygame.image.load(os.path.join("images",
            "player.jpg"))
        # Initialize the opponent's portrait image, depending on the opponent
        # argument passed.
        if opponent == 'timbersaw':
            self.opponent_portrait = pygame.image.load(os.path.join("images",
                "timbersaw.jpg"))
        elif opponent == 'storm_spirit':
            self.opponent_portrait = pygame.image.load(os.path.join("images",
                "storm_spirit.jpg"))
        elif opponent == 'self':
            self.opponent_portrait = pygame.image.load(os.path.join("images",
                "player.jpg"))
        # Make the opponent's image smaller
        self.opponent_portrait = pygame.transform.smoothscale(
            self.opponent_portrait, (110, 130))
        # Transform the dimensions of the player's portrait so that it is equal
        # to the size of the opponent's.
        self.player_portrait = pygame.transform.smoothscale(
            self.player_portrait, self.opponent_portrait.get_size())
        # Initialize the player's name text.
        self.player_name = name_text_font.render("The Player", 1, BLACK)
        # Initialize the opponent's name text, depending on the opponent
        if opponent == 'storm_spirit':
            self.opponent_name = name_text_font.render("Storm Spirit", 1,
                BLACK)
        else:
            self.opponent_name = name_text_font.render(opponent.capitalize(),
                1, BLACK)
        # Initialize the player's score text.
        self.player_score = score_text_font.render(str(game.player_score),
            1, RED)
        # Initialize the opponent's score text.
        self.opponent_score = score_text_font.render(str(game.opponent_score),
            1, BLUE)
        # Initialize the quit text.
        self.quit = menu_text_font.render("Quit?", 1, BLACK)
        # Initialize the win message for the player
        self.player_win = name_text_font.render("You win!", 1, RED)
        # Initialize the lose message for the player
        if opponent == 'storm_spirit':
            self.player_lose = name_text_font.render("Storm Spirit wins!",
                1, BLUE)
        else:
            self.player_lose = name_text_font.render(opponent.capitalize() + 
                " wins!", 1, BLUE)
        # Initialize the marks on the game board.
        self.mark_x = pygame.transform.smoothscale(pygame.image.load(
            os.path.join("images", "cross.png")), (80,80))
        self.mark_o = pygame.transform.smoothscale(pygame.image.load(
            os.path.join("images", "circle.png")), (80,80))

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
    click_sound = pygame.mixer.Sound(os.path.join("sound", "click.ogg"))
    # DEBUG: Print the sound path
    print("Click sound loaded from: " + os.path.join("sound", "click.ogg"))

    # Initialize the Timbersaw and Storm Spirit AIs
    timbersaw = Timbersaw()
    storm_spirit = StormSpirit()

    # Initialize the game board
    game = TicTacToe()

    # A boolean variable to check whether the player has made their move or not
    moved = 0

    # A boolean variable to check whether the player wanted to quit
    quit = 0

    # DEBUG: Constant testing values
    #game.board['topleft'] = 'x'
    #game.board['topcenter'] = 'o'
    #game.board['topright'] = 'x'
    #game.board['middleleft'] = 'o'
    #game.board['middlecenter'] = 'x'
    #game.board['middleright'] = 'o'
    #game.board['bottomleft'] = 'x'
    #game.board['bottomcenter'] = 'o'
    #game.board['bottomright'] = 'x'

    # Start the main game loop
    while 1:
        # Drawing stuff
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
        elif current_game_screen == 'timbersaw':
            # The player wanted to play against timbersaw
            # Draw the game screen
            game_screen = GameScreen(current_game_screen, game)
            game_screen.draw(game)
        elif current_game_screen == 'storm_spirit':
            # The player wanted to play against Storm Spirit
            # Draw the game screen
            game_screen = GameScreen(current_game_screen, game)
            game_screen.draw(game)

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
                            # Change the current screen according to the option
                            # chosen
                            if(main_menu.text_strings[main_menu.
                                    text_positions.index(pos)] ==
                                    main_menu.text_strings[0]):
                                # User chose to play against Timbersaw
                                current_game_screen = "timbersaw"
                            elif(main_menu.text_strings[main_menu.
                                   text_positions.index(pos)] ==
                                   main_menu.text_strings[1]):
                                # User chose to play against Storm Spirit
                                current_game_screen = "storm_spirit"
                            elif(main_menu.text_strings[main_menu.
                                    text_positions.index(pos)] ==
                                    main_menu.text_strings[2]):
                                # User chose to play against himself
                                current_game_screen = "self"
                            print('Screen changed to ' + current_game_screen)
                            # Play a sound
                            click_sound.play()
                elif(current_game_screen == 'timbersaw' or current_game_screen
                        == 'storm_spirit'):
                    # Check whether we have pressed quit
                    if((eventX > quit_rect.left and eventX <
                            quit_rect.right) and (eventY > quit_rect.top and
                            eventY < quit_rect.bottom)):
                        quit = 1
                        current_game_screen = "main"
                    else:
                        # Check whether we have pressed one of the tiles in the
                        # grid
                        for location_rect in location_rects:
                            if((eventX > location_rect.left and eventX <
                                    location_rect.right) and (eventY >
                                    location_rect.top and eventY <
                                    location_rect.bottom)):
                                # We have clicked one of the locations
                                if(game.board[location_names[location_rects.
                                        index(location_rect)]] == '-'):
                                    # The location is empty, let's mark it with
                                    # the player's mark
                                    game.board[location_names[location_rects.
                                        index(location_rect)]] = 'o'
                                    # Set the player's 'moved' flag
                                    moved = 1

        if not quit:
            # Game flow controller
            if not (game.check_winner('x') or game.check_winner('o')):
                # There is still no winner in the game.
                # Keep going with the game flow.
                if moved:
                    # Player has made their move, the other player should make
                    # their move now.
                    # Let's check who the opponent is.
                    if current_game_screen == 'timbersaw':
                        timbersaw.move(game.board)
                    elif current_game_screen == 'storm_spirit':
                        storm_spirit.move(game.board)
                    # Reset the moved flag
                    moved = 0
                    # Display a CLI view of the board
                    game.display_board()
            else:
                # Increment the winner's score.
                if game.check_winner('x'):
                    game.opponent_score += 1
                elif game.check_winner('o'):
                    game.player_score += 1
                # Reset the moved flag
                moved = 0
                pygame.display.flip()
                # Put a 3 sec delay
                pygame.time.wait(1500)
                # Reset the board
                game.clear_board()
        else:
            # Player chose to quit
            # Clear the game board
            moved = 0
            game.clear_board()
            game.reset_scores()
            quit = 0

        # Check if the board is full, reset if necessary
        if game.is_board_full():
            pygame.time.wait(1500)
            game.clear_board()
        
        # Update everything
        pygame.display.flip()

        # Tick the clock
        clock.tick(FPS)

if __name__ == '__main__':
    main()
