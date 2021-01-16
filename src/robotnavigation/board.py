"""
Main function for playing robot
"""
import os
import sys
import yaml
from typing import Dict, Any

from robotnavigation.entity import Entity
from robotnavigation.command import parse_cmd, verify_first_action

CONFIG_FILE = './user_config.yml'

class Board:
    def __init__(self) -> None:
        # read env
        env = self.load_env()
        
        # board size
        self.X = env['BOARD']['SIZE_X'] - 1
        self.Y = env['BOARD']['SIZE_Y'] - 1
        
        # init robot
        self.agent = Entity(self)
        
        # get inputs
        self.input_file = env['INPUT']

        
    def load_env(self) -> Dict[str, Any]:
        """
        Load environment file for board setup
        """
        with open(CONFIG_FILE) as file:
            env = yaml.full_load(file)
        return env
    
    def play(self) -> None:
        """
        Play robot given input file from environment
        """
        with open(self.input_file, 'r') as f:
            for i, line in enumerate(f):
                cmd_str = line.strip()
                if i == 0 and not verify_first_action(cmd_str):
                    raise ValueError('Robot must be placed at location: (0,0) and direction: NORTH')
                # parse command
                cmd = parse_cmd(cmd_str)
                
                if cmd is None:
                    continue # for invalid command just ignore
                    
                # execute action
                feed = self.agent.act(cmd)
                
                # for report action only
                if feed is not None:
                    sys.stdout.write(feed + '\n') 
                    
                    
if __name__ == '__main__':
    game = Board()
    game.play()