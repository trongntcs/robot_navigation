import os
import re
import logging
import yaml

from typing import List, Dict, Any, Tuple

USER_CONFIG_FILE = 'user_config.yml'
        
    
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

def get_logger(log_path):
    """Set the logger to log info in terminal and file `log_path`.
    In general, it is useful to have a logger so that every output to the terminal is saved
    in a permanent file. Here we save it to `model_dir/train.log`.
    Example:
    ```
    logging.info("Starting training...")
    ```
    Args:
        log_path: (string) where to log
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        # Logging to a file
        file_handler = logging.FileHandler(log_path)
        file_handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s: %(message)s'))
        logger.addHandler(file_handler)
