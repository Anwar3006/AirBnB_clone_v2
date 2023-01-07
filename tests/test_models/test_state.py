#!/usr/bin/python3
""" """
import unittest
import os
from models.base_model import BaseModel
from models.state import State
import pycodestyle


class Test_state(unittest.TestCase):
    """Tests for the State class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the State class"""
        cls.state = State()
        cls.state.name = 'Connecticut'

    @classmethod
    def tearDownClass(cls):
        """Tear down the setup after tests"""
        del cls.state

    def tearDown(self):
        """ """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pycodestyle_State(self):
        """Test State class for pep8 compliance"""
        style_check = pycodestyle.StyleGuide(quiet=True)
        result = style_check.check_file(['models/state.py'])
        self.assertEqual(result.total_errors, 0, 'Fix Pycodestyle')

    def test_for_doc(self):
        """Test for docstrings"""
        self.assertIsNone(self.state.__doc__)

    def test_for_attributes(self):
        """Test for attributes in dict"""
        self.assertTrue('name' in self.state.__dict__)
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)

    def test_for_subclass(self):
        """Test if State is subclass"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_attribute_type(self):
        """Test the types of the attributes"""
        self.assertTrue(type(self.state.name), str)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE' == 'db'),
                    'This test should only execute got FileStorage')
    def test_save_State(self):
        """Test if save works"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict(self):
        """Test if to_dict is in state dir"""
        self.assertTrue('to_dict' in dir(self.state), True)

if __name__ == "__main__":
    unittest.main()