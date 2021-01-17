import os
import argparse

from robotnavigation.board import Board

# config if starting from args
parser = argparse.ArgumentParser()
parser.add_argument('--size-x', type=int, default=100, help="Size for horizontal dimension")
parser.add_argument('--size-y', type=int, default=100, help="Size for vertical dimension")
parser.add_argument('--input-file', type=str, default='../inputs/test_0/input_0.txt', help="Input file of commands for robot")

    
def main_arg():
    print('***Run agent from args')
    args = parser.parse_args()
    game = Board.from_config(vars(args))
    print(str(game))
    print('>>> Playing agent')
    game.play()
    
if __name__ == '__main__':
    main_arg()
    