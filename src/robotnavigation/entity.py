"""
Agent handling
"""
from typing import Tuple, Any

from .action import Action
from .direction import Direction


class Entity:
    def __init__(self, board) -> None:
        # get board info
        self.LIMIT_X = board._X
        self.LIMIT_Y = board._Y
        
        # default init location
        self._x = 0 # current-x of robot
        self._y = 0 # current-y of robot
        self.direction = Direction.NORTH
        
        # index of direction in GLOBAL
        self.dir_index = 0 
        
    def _is_valid_location(self, _x: int, _y: int) -> bool:
        """
        Check if the location is valid
        """
        if _x < 0 or _x > self.LIMIT_X:
            return False
        if _y < 0 or _y > self.LIMIT_Y:
            return False
        
        return True
        
    def _moving(self) -> Tuple[int,int]:
        """
        Moving robot based on its current location and direction
        """
        if self.direction == Direction.NORTH:
            _x = self._x
            _y = self._y + 1
        elif self.direction == Direction.EAST:
            _x = self._x + 1
            _y = self._y
        elif self.direction == Direction.SOUTH:
            _x = self._x
            _y = self._y - 1
        elif self.direction == Direction.WEST:
            _x = self._x - 1
            _y = self._y
            
        if not self._is_valid_location(_x, _y):
            return self._x, self._y # return current location without taking any action
        
        return _x, _y
    
    def __str__(self) -> str:
        printable = [
            f'X: {self._x}',
            f'Y: {self._y}',
            f'Direction: {self.direction}'
        ]
        
        return ' '.join(printable)
        
    def act(self, cmd: Tuple[Any,...]) -> str:
        """
        Take action on robot via command
        """
        # get action-type
        action = cmd[0]
        
        if action == Action.REPORT:
            return str(self)
        
        if action == Action.PLACE:
            # fetch other-info in tuple
            _x, _y, direction = cmd[1], cmd[2], cmd[3]

            if not self._is_valid_location(_x, _y):
                raise ValueError(f'Location ({_x},{_y}) is not valid')

            # assign new location
            self._x = _x
            self._y = _y
            self.direction = direction
            self.dir_index = Direction.GLOBAL2INDEX[self.direction]

        elif action == Action.LEFT:
            self.dir_index = (self.dir_index - 1) % len(Direction.GLOBAL)
            self.direction = Direction.GLOBAL[self.dir_index]

        elif action == Action.RIGHT:
            self.dir_index = (self.dir_index + 1) % len(Direction.GLOBAL)
            self.direction = Direction.GLOBAL[self.dir_index]

        elif action == Action.MOVE:
            self._x, self._y = self._moving()

        else:
            raise ValueError(f'Action {action} is not supported')

        return None
                
    