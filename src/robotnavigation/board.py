"""
Main function for playing robot
"""
import pdb
import os
import sys
import logging
import time
from datetime import timedelta
from typing import Dict, Any, Union

from .entity import Entity
from .command import parse_cmd, verify_first_action
from .utils import (
    load_env, 
    load_env_from_arg,
    get_logger
)

class Board:
    def __init__(self, **kwargs) -> None:
        
        # load board via config file
        self.X = kwargs.pop('size_x', 100)
        self.Y = kwargs.pop('size_y', 100)
        self.input_file = kwargs.pop('input_file', None)
        
        # init agent
        self.agent = Entity(self)
        
        # get logger
        get_logger(os.path.join(os.path.dirname(self.input_file), 'run.log'))
            
    @classmethod
    def from_config(cls, input_env: Union[str, Dict[str, Any]]) -> "Board":
        if isinstance(input_env, str):
            # load from file
            env = load_env(input_env)
            if env is None:
                raise AssertionError('Config file is invalid')
                
            x = env['BOARD']['SIZE_X'] - 1
            y = env['BOARD']['SIZE_Y'] - 1
            input_file = env['INPUT']

        else:
            # load from args
            env = load_env_from_arg(**input_env)
            if env is None:
                raise AssertionError('Some errors found in arguments')
                
            x, y, input_file = (env if env is not None else (None, None, None))
            x = x - 1
            y = y - 1
        
        cfg_dict = {
            'size_x': x,
            'size_y': y,
            'input_file': input_file
        }
        return cls(**cfg_dict)
    
    def __str__(self) -> str:
        _info = f'BOARD: \n- SIZE: ({self.X}, {self.Y})\n- FILE: {self.input_file}\n'
        _info += f'AGENT: \n{str(self.agent)}'
        
        return _info
    
    def play(self) -> None:
        """
        Play robot given input file from environment
        """
        logging.info('Run agent from input file: %s', self.input_file)
        start_time = time.time()
        with open(self.input_file, 'r') as f:
            for i, line in enumerate(f):
                cmd_str = line.strip()
                if i == 0 and not verify_first_action(cmd_str):
                    raise ValueError('Robot must be placed at location: (0,0) and direction: NORTH')
                # parse command
                cmd = parse_cmd(cmd_str)
                
                if cmd is None:
                    logging.info("Command '%s' is invalid to proceed and will be irgnored", cmd_str)
                    continue # for invalid command just ignore
                
                try:
                    # execute action
                    feed = self.agent.act(cmd)

                    # for report action only
                    if feed is not None:
                        sys.stdout.write(feed + '\n') 
                except Exception as e:
                    logging.info("An exception found in the command '%s': %s", cmd_str, str(e))
                    pass
                    
        logging.info('--- Finish in %.6f seconds ---', (time.time() - start_time))