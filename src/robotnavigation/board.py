"""
Main function for playing robot
"""
import os
import sys
import logging
import time
from typing import Dict, Any, Union

from .entity import Entity
from .command import parse_cmd, verify_first_action
from .utils import (
    load_env,
    load_env_from_arg,
    get_logger
)

class Board:
    """
    Board class for managing robot
    """
    def __init__(self, **kwargs) -> None:
        # load board via config file
        self._X = kwargs.pop('size_x', 100)
        self._Y = kwargs.pop('size_y', 100)
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
                
            _x = env['BOARD']['SIZE_X'] - 1
            _y = env['BOARD']['SIZE_Y'] - 1
            input_file = env['INPUT']
            
        else:
            # load from args
            env = load_env_from_arg(**input_env)
            if env is None:
                raise AssertionError('Some errors found in arguments')
                
            _x, _y, input_file = (env if env is not None else (None, None, None))
            _x = _x - 1
            _y = _y - 1
            
        cfg_dict = {
            'size_x': _x,
            'size_y': _y,
            'input_file': input_file
        }
        return cls(**cfg_dict)
    
    def __str__(self) -> str:
        _info = f'BOARD: \n- SIZE: ({self._X}, {self._Y})\n- FILE: {self.input_file}\n'
        _info += f'AGENT: \n{str(self.agent)}'
        
        return _info
    
    def play(self) -> None:
        """
        Play robot given input file from environment
        """
        logging.info('Run agent from input file: %s', self.input_file)
        start_time = time.time()
        with open(self.input_file, 'r') as _f:
            
            for i, line in enumerate(_f):
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
                        
                except Exception as error:
                    logging.info("An exception found in the command '%s': %s", cmd_str, str(error))
                    
        logging.info('--- Finish in %.6f seconds ---', (time.time() - start_time))
        