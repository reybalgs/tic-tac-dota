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
        self.player_score = 0
        self.opponent_score = 0
        self.player_spree = 0
        self.opponent_spree = 0

    def get_location_key(self, location_num):
        """
        Evaluates the location integer specified and returns the key pertaining
        to the location.
        """
        if location_num == 1:
            return 'topleft'
        elif location_num == 2:
            return 'topcenter'
        elif location_num == 3:
            return 'topright'
        elif location_num == 4:
            return 'middleleft'
        elif location_num == 5:
            return 'middlecenter'
        elif location_num == 6:
            return 'middleright'
        elif location_num == 7:
            return 'bottomleft'
        elif location_num == 8:
            return 'bottomcenter'
        elif location_num == 9:
            return 'bottomright'

    def is_location_occupied(self, location_num):
        """
        Checks if the specified location integer is occupied or not. Returns
        either true or false.

        Take note that the locations are defined as follows:
        
        1|2|3
        4|5|6
        7|8|9
        """
        if(location_num == 1):
            if(self.board['topleft'] != '-'):
                return True
            else:
                return False
        elif(location_num == 2):
            if(self.board['topcenter'] != '-'):
                return True
            else:
                return False
        elif(location_num == 3):
            if(self.board['topright'] != '-'):
                return True
            else:
                return False
        elif(location_num == 4):
            if(self.board['middleleft'] != '-'):
                return True
            else:
                return False
        elif(location_num == 5):
            if(self.board['middlecenter'] != '-'):
                return True
            else:
                return False
        elif(location_num == 6):
            if(self.board['middleright'] != '-'):
                return True
            else:
                return False
        elif(location_num == 7):
            if(self.board['bottomleft'] != '-'):
                return True
            else:
                return False
        elif(location_num == 8):
            if(self.board['bottomcenter'] != '-'):
                return True
            else:
                return False
        elif(location_num == 9):
            if(self.board['bottomright'] != '-'):
                return True
            else:
                return False

    def display_board(self):
        """
        Displays an ASCII representation of the board. Useful for debugging
        without the UI.
        """
        print(self.board['topleft'] + self.board['topcenter'] +
              self.board['topright'])
        print(self.board['middleleft'] + self.board['middlecenter']
              + self.board['middleright'])
        print(self.board['bottomleft'] + self.board['bottomcenter']
              + self.board['bottomright'])

    def reset_scores(self):
        """
        Resets the scores of the player and the opponent.
        """
        self.player_score = 0
        self.opponent_score = 0
        self.player_spree = 0
        self.opponent_spree = 0

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

