"""
Test Agent Behaviors
"""

import os
import sys
import pytest
import unittest
from io import StringIO

from robotnavigation.board import Board
from robotnavigation.utils import load_env

VALID_TEST = os.path.join(os.path.dirname(__file__), 'fixtures/sample_env')
INVALID_TEST = os.path.join(os.path.dirname(__file__), 'fixtures/invalid_env')

ARG_ENV = {
    "size_x": 100,
    "size_y": 200,
    "input_file": os.path.join(os.path.dirname(__file__), f'fixtures/input.txt')
}

class TestAgent(unittest.TestCase):
    
    def setUp(self):
        # valid case
        self.board = Board.from_config(VALID_TEST)
        # invalid case
        self.in_board = Board.from_config(INVALID_TEST)
        # load from args
        self.arg_board = Board.from_config(ARG_ENV)
        
    def test_boad(self):
        
        self.assertEqual(self.board._X, 99)
        self.assertEqual(self.board._Y, 199)
        self.assertTrue(os.path.exists(self.board.input_file), 'Input file does not exist')
        
    def test_play(self):
        
        save_stdout = sys.stdout
        out = StringIO()
        sys.stdout = out
        
        self.board.play()
        
        res = out.getvalue().strip().split('\n')
        self.assertEqual(res[0], 'X: 0 Y: 1 Direction: WEST')
        self.assertEqual(res[1], 'X: 98 Y: 199 Direction: NORTH')
        sys.stdout = save_stdout
        
    def test_invalid_first_cmd(self):
        
        with self.assertRaises(ValueError):
            self.in_board.play()
            
    def test_play_from_arg(self):
        
        save_stdout = sys.stdout
        out = StringIO()
        sys.stdout = out
        
        self.arg_board.play()
        
        res = out.getvalue().strip().split('\n')
        self.assertEqual(res[0], 'X: 0 Y: 1 Direction: WEST')
        self.assertEqual(res[1], 'X: 98 Y: 199 Direction: NORTH')
        sys.stdout = save_stdout
        