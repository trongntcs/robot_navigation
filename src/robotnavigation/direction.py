"""
Define all valid directions
"""

class Direction:
    NORTH = "NORTH"
    EAST = "EAST"
    SOUTH = "SOUTH"
    WEST = "WEST"
    GLOBAL = [NORTH, EAST, SOUTH, WEST]
    GLOBAL2INDEX = dict(zip(GLOBAL, range(len(GLOBAL))))
