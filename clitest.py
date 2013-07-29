#!/usr/bin/python

# clitest.py
#
# Used to test the AI and the game logic in a CLI environment

import random, sys, os
from ai_timbersaw import *
from tictactoe_game import *
from ai_stormspirit import *

def start_game(game, ai):
    game.clear_board()
    print('Board is cleared.')

    while(not game.check_winner('o') and not game.check_winner('x') and not
            game.is_board_full()):
        game.display_board()
        option = 0
        print('Player turn')

        while (option <= 0 or option > 9):
            option = int(raw_input('Input location of choice: '))

        if not game.is_location_occupied(option):
            game.board[game.get_location_key(option)] = 'o'

        if not game.check_winner('o'):
            print('AI turn')
            ai.move(game.board)
        
        game.display_board()

    if game.check_winner('o'):
        return 'o'
    elif game.check_winner('x'):
        return 'x'
    elif game.is_board_full():
        return 'draw'

def main():
    game = TicTacToe()
    player_score = 0
    ai_score = 0
    option = raw_input('Play against [a] Timbersaw [b] Storm Spirit: ')

    if option is 'a':
        ai = Timbersaw()
    else:
        ai = StormSpirit()
    
    play = 1
    while play:
        print('Player: ' + str(player_score) + '\n' + ai.name + ': ' + 
                str(ai_score))
        win = start_game(game, ai)
        if win == 'o':
            print('You win')
            player_score += 1
        elif win == 'x':
            print(ai.name + ' wins')
            ai_score += 1
        else:
            print('Draw')
        option = raw_input('Play again [y/n]? ')
        if option is not 'y':
            play = 0

    print('CLI testing over')

if __name__ == '__main__':
    main()
