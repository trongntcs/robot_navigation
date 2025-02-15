"""
Transform/parse text to command format
"""
import os
import re
from typing import Tuple

from .action import Action
from .direction import Direction

"""
Define all command patterns accepted
"""
CMD_RE_LIST = [
    f'^({Action.PLACE})'
    + r'\s+(\d+)\s+(\d+)\s+'
    + f'({Direction.NORTH}'
    + f'|{Direction.EAST}'
    + f'|{Direction.SOUTH}'
    + f'|{Direction.WEST})$',
    f'^({Action.MOVE}|{Action.LEFT}|{Action.RIGHT}|{Action.REPORT})$'
]

CMD_RE = '|'.join(CMD_RE_LIST)

    
def is_valid_cmd(cmd_str: str) -> bool:
    """
    Check if the command is valid
    """
    return re.compile(CMD_RE).match(cmd_str) is not None

def parse_cmd(cmd_str: str) -> Tuple[str, ...]:
    """
    Parse command from text
    """
    if not is_valid_cmd(cmd_str):
        return None

    if re.match(CMD_RE_LIST[0], cmd_str) is not None:
        action, loc_x, loc_y, direction = re.match(CMD_RE_LIST[0], cmd_str).groups()
        return (action, int(loc_x), int(loc_y), direction)

    else:
        action = re.match(CMD_RE_LIST[1], cmd_str).group(1)
        return (action, )
    
def verify_first_action(cmd_str: str) -> bool:
    """
    Check if first command is valid
    """
    subre = r'\s+0\s+0\s+'
    return re.match(f'{Action.PLACE}{subre}{Direction.NORTH}', cmd_str) is not None

