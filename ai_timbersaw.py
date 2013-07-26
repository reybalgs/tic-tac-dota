#
# ai_timbersaw.py
#
# Contains the AI routines and behavior for Timbersaw, the cautious AI player

import random

class Timbersaw():
    """
    The cautious AI.
    """
    def find_line_attempt(self, board, player_mark='o'):
        """
        Looks for the other player's attempts at creating lines. Returns the
        string of the key of the location where the AI should mark.
        """
        # Initialize the location
        move = ''

        # Horizontal combinations
        # First possible combination: Topleft and topcenter
        if(board['topleft'] == player_mark and board['topcenter'] ==
           player_mark and board['topright'] == '-'):
            move = 'topright'
            print('Discovered topleft and topcenter marks\n')

        # Second possible combination: Topleft and topright
        elif(board['topleft'] == player_mark and board['topright'] ==
             player_mark and board['topcenter'] == '-'):
            move = 'topcenter'
            print('Discovered topleft and topright marks\n')

        # Third possible combination: Topcenter and topright
        elif(board['topcenter'] == player_mark and board['topright'] ==
             player_mark and board['topleft'] == '-'):
            move = 'topleft'
            print('Discovered topcenter and topright marks\n')

        # Fourth possible combination: Middleleft and middlecenter
        elif(board['middleleft'] == player_mark and board['middlecenter'] ==
             player_mark and board['middleright'] == '-'):
            move = 'middleright'
            print('Discovered middleleft and middlecenter marks\n')

        # Fifth possible combination: Middleleft and middleright
        elif(board['middleleft'] == player_mark and board['middleright'] ==
             player_mark and board['middlecenter'] == '-'):
            move = 'middlecenter'
            print('Discovered middleleft and middleright marks\n')

        # Sixth possible combination: Middlecenter and middleright
        elif(board['middlecenter'] == player_mark and board['middleright'] ==
             player_mark and board['middleleft'] == '-'):
            move = 'middleleft'
            print('Discovered middlecenter and middleright marks\n')

        # Seventh possible combination: Bottomleft and bottomcenter
        elif(board['bottomleft'] == player_mark and board['bottomcenter'] ==
             player_mark and board['bottomright'] == '-'):
            move = 'bottomright'
            print('Discovered bottomleft and bottomcenter marks\n')

        # Eighth possible combination: Bottomleft and bottomright
        elif(board['bottomleft'] == player_mark and board['bottomright'] ==
             player_mark and board['bottomcenter'] == '-'):
            move = 'bottomcenter'
            print('Discovered bottomleft and bottomright marks\n')

        # Ninth possible combination: Bottomcenter and bottomright
        elif(board['bottomcenter'] == player_mark and board['bottomright'] ==
                player_mark and board['bottomright'] == '-'):
            move = 'bottomright'
            print('Discovered bottomcenter and bottomright marks\n')

        # Vertical combinations
        # Tenth possible combination: Topleft and middleleft
        elif(board['topleft'] == player_mark and board['middleleft'] ==
             player_mark and board['bottomleft'] == '-'):
            move = 'bottomleft'
            print('Discovered topleft and middleleft marks')

        # Eleventh possible combination: Topleft and bottomleft
        elif(board['topleft'] == player_mark and board['bottomleft'] ==
             player_mark and board['middleleft'] == '-'):
            move = 'middleleft'
            print('Discovered topleft and bottomleft marks\n')

        # Twelveth possible combination: Middleleft and bottomleft
        elif(board['middleleft'] == player_mark and board['bottomleft'] ==
             player_mark and board['topleft'] == '-'):
            move = 'topleft'
            print('Discovered middleleft and bottomleft marks\n')

        # Thirteenth possible combination: Topcenter and middlecenter
        elif(board['topcenter'] == player_mark and board['middlecenter'] ==
             player_mark and board['bottomcenter'] == '-'):
            move = 'bottomcenter'
            print('Discovered topcenter and middlecenter marks\n')

        # Fourteenth possible combination: Topcenter and bottomcenter
        elif(board['topcenter'] == player_mark and board['bottomcenter'] ==
             player_mark and board['middlecenter'] == '-'):
            move = 'middlecenter'
            print('Discovered topcenter and bottomcenter marks\n')

        # Fifteenth possible combination: Middlecenter and bottomcenter
        elif(board['middlecenter'] == player_mark and board['bottomcenter']
             == player_mark and board['topcenter'] == '-'):
            move = 'topcenter'
            print('Discovered middlecenter and bottomcenter marks\n')

        # Sixteenth possible combination: Topright and middleright
        elif(board['topright'] == player_mark and board['middleright'] ==
             player_mark and board['bottomright'] == '-'):
            move = 'bottomright'
            print('Discovered topright and middleright marks\n')

        # Seventeenth possible combination: Topright and bottomright
        elif(board['topright'] == player_mark and board['bottomright'] ==
             player_mark and board['middleright'] == '-'):
            move = 'middleright'
            print('Discovered topright and bottomright marks\n')

        # Eighteenth possible combination: Middleright and bottomright
        elif(board['middleright'] == player_mark and board['bottomright'] ==
             player_mark and board['topright'] == '-'):
            move = 'topright'
            print('Discovered middleright and bottomright marks\n')

        # Diagonal combinations
        # Nineteenth possible combination: Topleft and middlecenter
        elif(board['topleft'] == player_mark and board['middlecenter'] ==
             player_mark and board['bottomright'] == '-'):
            move = 'bottomright'
            print('Discovered topleft and middlecenter marks\n')

        # Twentieth possible combination: Topleft and bottomright
        elif(board['topleft'] == player_mark and board['bottomright'] ==
             player_mark and board['middlecenter'] == '-'):
            move = 'middlecenter'
            print('Discovered topleft and bottomright marks\n')

        # Twenty-first possible combination: Middlecenter and bottomright
        elif(board['middlecenter'] == player_mark and board['bottomright'] ==
             player_mark and board['topleft'] == '-'):
            move = 'topleft'
            print('Discovered middlecenter and bottomright marks\n')

        # Twenty-second possible combination: Bottomleft and middlecenter
        elif(board['bottomleft'] == player_mark and board['middlecenter'] ==
             player_mark and board['topright'] == '-'):
            move = 'topright'
            print('Discovered bottomleft and middlecenter marks\n')

        # Twenty-third possible combination: Bottomleft and topright
        elif(board['bottomleft'] == player_mark and board['topright'] ==
             player_mark and board['middlecenter'] == '-'):
            move = 'middlecenter'
            print('Discovered bottomleft and topright marks\n')

        # Twenty-fourth possible combination: Middlecenter and topright
        elif(board['middlecenter'] == player_mark and board['topright'] ==
             player_mark and board['bottomleft'] == '-'):
            move = 'bottomleft'
            print('Discovered middlecenter and topright marks\n')

        # Return the possible location
        return move

    def move(self, board, player_mark='o'):
        """
        Function that is called whenever the AI is supposed to make a move.

        Requires the board as a parameter. The board is a copy of the board
        dict used by the tictactoe game board.

        Also requires the player's mark as a parameter. This is 'o' by
        default.  
        """
        # First, the AI has to check whether the player has formed a line.
        # The AI does this by analyzing all the marks that the player has
        # created.
        
        # Initialize a move variable that determines the location that the AI
        # will mark
        move = ''

        # Look for any attempts of the player to create a line, and find the
        # best location to mark in order to block that attempt
        print('Looking for opponent line attempts...')
        move = self.find_line_attempt(board)

        # Now let's check if we actually found any attempts
        if(move == ''):
            # Let's check if we can find one of our own line attempts. If there
            # are any, we will mark that location
            print('No opponent line attempts found. Will now check for self' +
                    ' line attempts to follow up')
            move = self.find_line_attempt(board, 'x')

            if(move == ''):
                print('No self line attempts found. Will now mark random ' +
                        'location')
                # If we have found none, then randomly pick an unoccupied
                # spot to mark
                marked = 0
                while marked == 0:
                    location = random.randint(1,9)
                    # The location will have to be empty
                    if(location == 1 and board['topleft'] == '-'):
                        marked = 1
                        print('Marking topleft location\n')
                    elif(location == 2 and board['topcenter'] == '-'):
                        marked = 1
                        print('Marking topcenter location\n')
                    elif(location == 3 and board['topright'] == '-'):
                        marked = 1
                        print('Marking topright location\n')
                    elif(location == 4 and board['middleleft'] == '-'):
                        marked = 1
                        print('Marking middleleft location\n')
                    elif(location == 5 and board['middlecenter'] == '-'):
                        marked = 1
                        print('Marking middlecenter location\n')
                    elif(location == 6 and board['middleright'] == '-'):
                        marked = 1
                        print('Marking middleright location\n')
                    elif(location == 7 and board['bottomleft'] == '-'):
                        marked = 1
                        print('Marking bottomleft location\n')
                    elif(location == 8 and board['bottomcenter'] == '-'):
                        marked = 1
                        print('Marking bottomcenter location\n')
                    elif(location == 9 and board['bottomright'] == '-'):
                        marked = 1
                        print('Marking bottomright location\n')
                    else:
                        # There are no more locations to mark, but set marked to
                        # true anyway
                        marked = 1
                        print('No empty spaces found!')
                    # Mark the location chosen
                    if(location == 1):
                        board['topleft'] = self.mark
                    elif(location == 2):
                        board['topcenter'] = self.mark
                    elif(location == 3):
                        board['topright'] = self.mark
                    elif(location == 4):
                        board['middleleft'] = self.mark
                    elif(location == 5):
                        board['middlecenter'] = self.mark
                    elif(location == 6):
                        board['middleright'] = self.mark
                    elif(location == 7):
                        board['bottomleft'] = self.mark
                    elif(location == 8):
                        board['bottomcenter'] = self.mark
                    elif(location == 9):
                        board['bottomright'] = self.mark
            else:
                # Mark the location
                board[move] = self.mark
                print('Marked location at ' + move)
        else:
            # Mark the location
            board[move] = self.mark
            print('Marked location at ' + move)

    def __init__(self, mark='x'):
        """
        Default initializing constructor.
        """
        # Set the mark of the AI to the specified argument
        self.mark = mark
        print('AI Timbersaw (Cautious) initialized')
