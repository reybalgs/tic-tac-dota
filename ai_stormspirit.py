# ai_stormspirit.py
#
# Contains the AI for Storm Spirit, the dumb and aggressive AI.

from ai_timbersaw import *

class StormSpirit(Timbersaw):
    """
    The class for the Storm Spirit. Inherits methods from Timbersaw, but not
    designed to use the check line method.
    """
    def move(self, board, player_mark='o'):
        """
        Function that is called whenever the AI is supposed to make a move.

        Requires the board as a parameter. The board is a copy of the board
        dict used by the tictactoe game board.

        Also requires the player's mark as a parameter. This is 'o' by
        default.
        """
        # Storm Spirit is a dumb yet aggressive AI, so he does not need to
        # check whether the opponent has created a line.

        # Initialize a move variable that determines the location that the AI
        # will mark.
        move = ''

        # Let's see if there are any potential lines that we can form,
        # then mark the location that would finish that line.
        print('Searching for potential lines...')
        move = self.find_line_attempt(board, 'x')

        if(move == ''):
            print('No potential lines found. Marking random location.')
            # Initialize a boolean variable that tracks whether we have
            # marked a location or not.
            marked = 0
            while not marked:
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
            # We found a line attempt, let's mark the finishing location
            board[move] = self.mark
            print('Marked location at ' + move)

    def __init__(self, mark='x'):
        """
        Default initializing constructor.
        """
        # Set the mark of the AI to the argument provided
        self.mark = mark
        print('AI Storm Spirit (Aggressive) initialized')
