"""
Test environment loader
"""
import os
import unittest

from robotnavigation.utils import load_env, load_env_from_arg


CONFIG_FOLDER = os.path.join(os.path.dirname(__file__), 'fixtures/sample_env')

ARG_ENV = {
    "size_x": 100,
    "size_y": 200,
    "input_file": os.path.join(os.path.dirname(__file__), f'fixtures/input.txt')
}

class TestEnv(unittest.TestCase):
    
    def test_load_env(self):
        env = load_env(CONFIG_FOLDER)
        self.assertTrue(env is not None)
        
        self.assertIn("BOARD", env)
        self.assertIn("INPUT", env)
        self.assertIn("SIZE_X", env['BOARD'])
        self.assertIn("SIZE_Y", env['BOARD'])
        
        self.assertTrue(isinstance(env['BOARD']['SIZE_X'], int))
        self.assertTrue(isinstance(env['BOARD']['SIZE_Y'], int))
        self.assertTrue(isinstance(env['INPUT'], str))
        
        self.assertEqual(env['BOARD']['SIZE_X'], 100)
        self.assertEqual(env['BOARD']['SIZE_Y'], 200)
        self.assertTrue(env['INPUT'].endswith('sample_input.txt'))
        
    
    def test_load_env_from_arg(self):
        env = load_env_from_arg(**ARG_ENV)
        self.assertTrue(env is not None)
        x, y, input_file = env
        
        self.assertTrue(isinstance(x, int))
        self.assertTrue(isinstance(y, int))
        self.assertTrue(isinstance(input_file, str))
        
        self.assertEqual(x, 100)
        self.assertEqual(y, 200)
        self.assertTrue(input_file.endswith('input.txt'))
        