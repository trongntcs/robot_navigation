import os
import argparse

from robotnavigation.board import Board

# config if starting from cfg-folder
CONFIG_FILE = os.path.join(os.path.dirname(__file__), "../inputs/test_0")

def main_cfg():  
    print('***Run agent from config file')
    game = Board.from_config(CONFIG_FILE)
    print(str(game))
    print('>>> Playing agent')
    game.play()
        
if __name__ == '__main__':
    main_cfg()
    