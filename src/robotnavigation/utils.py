import os
import re
import yaml
from typing import List, Dict, Any, Tuple

USER_CONFIG_FILE = 'user_config.yml'

class Action:
    """
    Define all action-types
    """
    PLACE = "PLACE"
    MOVE = "MOVE"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    REPORT = "REPORT"
    
    
class Direction:
    """
    Define all valid directions
    """
    NORTH = "NORTH"
    EAST = "EAST"
    SOUTH = "SOUTH"
    WEST = "WEST"
    GLOBAL = [NORTH, EAST, SOUTH, WEST]
    GLOBAL2INDEX = dict(zip(GLOBAL, range(len(GLOBAL))))
    
    
def is_valid_env(env) -> bool:
    try:       
        assert env['BOARD']['SIZE_X'] > 0
        assert env['BOARD']['SIZE_Y'] > 0
        assert isinstance(env['INPUT'], str)
        
    except:
        return False
    
    return True
        
def load_env(env_file) -> Dict[str, Any]:
    """
    Load environment file for board setup
    """
    with open(os.path.join(env_file, USER_CONFIG_FILE)) as file:
        env = yaml.full_load(file)
        env["INPUT"] = os.path.join(env_file, env["INPUT"])
        
    return env if is_valid_env(env) else None

def load_env_from_arg(**kwargs) -> Tuple[int, int, str]:
    
    x = kwargs.pop('size_x', -1)
    y = kwargs.pop('size_y', -1)
    input_file = kwargs.pop('input_file', None)
    try:
        assert x > 0
        assert y > 0
        assert isinstance(input_file, str)
    
    except:
        return None
    
    return (x, y, input_file)
