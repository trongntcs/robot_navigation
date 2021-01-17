"""
Test command parser
"""
import re
import unittest

from robotnavigation.command import parse_cmd, is_valid_cmd
from robotnavigation.action import Action
from robotnavigation.direction import Direction


class TestParser(unittest.TestCase):
    
    def test_valid_command(self):
        
        _cmds = [f'PLACE 100 100 {d}' for d in Direction.GLOBAL]
        for c in _cmds:
            self.assertTrue(is_valid_cmd(c), f'Command {c} should be valid')
        
        _cmd = 'MOVE'
        self.assertTrue(is_valid_cmd(_cmd), f'Command {_cmd} should be valid')
        
        _cmd = 'LEFT'
        self.assertTrue(is_valid_cmd(_cmd), f'Command {_cmd} should be valid')
        
        _cmd = 'RIGHT'
        self.assertTrue(is_valid_cmd(_cmd), f'Command {_cmd} should be valid')
        
        _cmd = 'REPORT'
        self.assertTrue(is_valid_cmd(_cmd), f'Command {_cmd} should be valid')
        
        
    def test_invalid_command(self):
        
        _cmds = [
            'PLACE 100 NORTH',
            'PLACE 100 100 100 NORTH',
            'MOVE 3',
            'PLACE 1 1 MOVE',
            'RIGHT 1',
            'REPORT 1'
        ] 
        _cmds += Direction.GLOBAL
        for c in _cmds:
            self.assertFalse(is_valid_cmd(c), f'Command {c} should be invalid')
            
    def test_valid_parser(self):
        
        _cmds = [f'PLACE 100 100 {d}' for d in Direction.GLOBAL]
        
        for c in _cmds:
            res = parse_cmd(c)
            self.assertEqual(len(res), 4)
            
            self.assertEqual(res[0], Action.PLACE, f'Action should be {Action.PLACE}')           
            self.assertEqual(res[1], 100)
            self.assertEqual(res[2], 100)
            self.assertIn(res[3], Direction.GLOBAL)
            
        for d in [Action.MOVE, Action.LEFT, Action.RIGHT, Action.REPORT]:
            res = parse_cmd(d)
            self.assertEqual(len(res), 1)
            self.assertIn(res[0], Action.__dict__, f'Action {d} should be valid')
            
        
            