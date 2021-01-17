import os
import argparse

from robotnavigation.board import Board
from robotnavigation.utils import load_env, load_env_from_arg

# config if starting from cfg-file
CONFIG_FILE = os.path.join(os.path.dirname(__file__), "../inputs/test_0")

# config if starting from args
parser = argparse.ArgumentParser()
parser.add_argument('--size-x', type=int, default=100, help="Size for horizontal dimension")
parser.add_argument('--size-y', type=int, default=100, help="Size for vertical dimension")
parser.add_argument('--input-file', type=str, default='../inputs/test_0/input_0.txt', help="Input file of commands for robot")

def main_cfg():  
    print('\n***Run agent from config file')
    game = Board.from_config(CONFIG_FILE)
    print(str(game))
    print('>>> Playing agent')
    game.play()
    
def main_arg():
    print('\n***Run agent from args')
    args = parser.parse_args()
    game = Board.from_config(vars(args))
    print(str(game))
    print('>>> Playing agent')
    game.play()
    
if __name__ == '__main__':
    main_cfg()
    main_arg()
    