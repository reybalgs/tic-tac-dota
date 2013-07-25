#
# tictactoe_game.py
#
# Contains the game logic for a tictactoe game.

class TicTacToe():
    """
    The class for a game of TicTacToe.

    Receives input from players, and outputs the game board as well as other
    information for both the human and AI players to use.
    """

    def __init__(self):
        """
        Default initialization constructor for a game.
        """
        # Initialize the game's board, a dictionary containing 9 key-pair
        # values where the location is the key and the contents of that
        # location is the value.
        #
        # All the locations are initialized with a blank value (-). Other
        # values are (o) and (x), pertaining to the circles and crosses.
        self.board = {'topleft':'-', 'topcenter':'-', 'topright':'-',
                'middleleft':'-', 'middlecenter':'-', 'middleright':'-',
                'bottomleft':'-', 'bottomcenter':'-', 'bottomright':'-'}

    def display_board(self):
        """
        Displays an ASCII representation of the board. Useful for debugging
        without the UI.
        """
        print('\n')
        print(self.board['topleft'] + self.board['topcenter'] +
              self.board['topright'])
        print(self.board['middleleft'] + self.board['middlecenter']
              + self.board['middleright'])
        print(self.board['bottomleft'] + self.board['bottomcenter']
              + self.board['bottomright'])

    def clear_board(self):
        """
        Clears the game board, removing all marks made by the players
        """
        self.board['topleft'] = '-'
        self.board['topcenter'] = '-'
        self.board['topright'] = '-'
        self.board['middleleft'] = '-'
        self.board['middlecenter'] = '-'
        self.board['middleright'] = '-'
        self.board['bottomleft'] = '-'
        self.board['bottomcenter'] = '-'
        self.board['bottomright'] = '-'

    def is_board_full(self):
        """
        Checks whether or not the board is full. Returns either true or false.
        """
        # Initially consider the board as full
        full = True

        for location in self.board.values():
            # Loop through all locations
            if location == '-':
                # If one of the locations are empty, full becomes false
                full = False

        return full

    def check_winner(self, player):
        """
        Checks if the player provided as an argument already won. The player
        argument is a char that is either 'x' or 'o'.

        It does this by checking all eight possible winning combinations in
        standard Tic Tac Toe for a line of the player.

        Returns either true or false whether or not the player won or not
        """

        # First combination: Topleft to bottomleft vertical line
        if(self.board['topleft'] == player and self.board['middleleft'] ==
                player and self.board['bottomleft'] == player):
            return True
        
        # Second combination: Topcenter to bottomcenter vertical line
        elif(self.board['topcenter'] == player and self.board['middlecenter']
                == player and self.board['bottomcenter'] == player):
            return True

        # Third combination: Topright to bottomright vertical line
        elif(self.board['topright'] == player and self.board['middleright'] ==
                player and self.board['bottomright'] == player):
            return True

        # Fourth combination: Topleft to topright horizontal line
        elif(self.board['topleft'] == player and self.board['topcenter'] ==
                player and self.board['topright'] == player):
            return True

        # Fifth combination: Middleleft to middleright horizontal line
        elif(self.board['middleleft'] == player and
                self.board['middlecenter'] == player and
                self.board['middleright'] == player):
            return True

        # Sixth combination: Bottomleft to bottomright horizontal line
        elif(self.board['bottomleft'] == player and
                self.board['bottomcenter'] == player and
                self.board['bottomright'] == player):
            return True

        # Seventh combination: Topleft to bottomright diagonal line
        elif(self.board['topleft'] == player and self.board['middlecenter'] ==
                player and self.board['bottomright'] == player):
            return True

        # Eighth combination: Bottomleft to topright diagonal line
        elif(self.board['bottomleft'] == player and
                self.board['middlecenter'] == player and
                self.board['topright'] == player):
            return True

        # Otherwise, looks like we haven't found a line
        else:
            return False

