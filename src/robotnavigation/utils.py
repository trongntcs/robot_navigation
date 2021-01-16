import re
from typing import List


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
    