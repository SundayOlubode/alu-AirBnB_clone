#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
#import os
from models.base_model import BaseModel



class TestFileStorage(unittest.TestCase):
    ''' Test File storage '''

    def test_pep8_FileStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "Check pep8")



if __name__ == "__main__":
    unittest.main()
