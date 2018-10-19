import unittest
import os

from src.main import get_cwd


class TestMain(unittest.TestCase):

    def test_get_cwd(self):
        print('testing get_cwd()')
        os.chdir('src')
        current_dir = get_cwd()
        self.assertIsNotNone(current_dir)
        self.assertEqual(current_dir, 'src')
