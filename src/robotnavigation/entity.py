
import os
import sys

from typing import Tuple, Any

from .utils import (
    Action,
    Direction
)

class Entity:
    def __init__(self, board) -> None:
        # get board info
        self.LIMIT_X = board.X
        self.LIMIT_Y = board.Y
        # default init location
        self.x = 0 # current-x of robot
        self.y = 0 # current-y of robot
        self.direction = Direction.NORTH
        self.index = 0 # index of direction in GLOBAL
        
    def _is_valid_location(self, x: int, y: int) -> bool:
        """
        Check if the location is valid
        """
        if x < 0 or x > self.LIMIT_X:
            return False
        if y < 0 or y > self.LIMIT_Y:
            return False
        
        return True
        
    def _moving(self) -> Tuple[int,int]:
        """
        Moving robot based on its current location and direction
        """
        if self.direction == Direction.NORTH:
            x = self.x
            y = self.y + 1
        elif self.direction == Direction.EAST:
            x = self.x + 1
            y = self.y
        elif self.direction == Direction.SOUTH:
            x = self.x
            y = self.y - 1
        elif self.direction == Direction.WEST:
            x = self.x - 1
            y = self.y
            
        if not self._is_valid_location(x, y):
            return self.x, self.y # return current location without taking any action
        
        return x, y
    
    def __str__(self):
        printable = [
            f'X: {self.x}',
            f'Y: {self.y}',
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
        
        else:
            if action == Action.PLACE:
                # fetch other-info in tuple
                x, y, direction = cmd[1], cmd[2], cmd[3]
                
                if not self._is_valid_location(x, y):
                    return None # simply ignore this action
                
                # assign new location
                self.x = x
                self.y = y
                self.direction = direction
                self.index = Direction.GLOBAL2INDEX[self.direction]

            elif action == Action.LEFT:
                self.index = (self.index - 1) % len(Direction.GLOBAL)
                self.direction = Direction.GLOBAL[self.index]

            elif action == Action.RIGHT:
                self.index = (self.index + 1) % len(Direction.GLOBAL)
                self.direction = Direction.GLOBAL[self.index]

            elif action == Action.MOVE:
                self.x, self.y = self._moving()
            
            else:
                raise ValueError(f'Action {action} is not valid')
                
            return None
                
    