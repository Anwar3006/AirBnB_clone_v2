#!/usr/bin/python3
"""Test for User"""

import unittest
import os
from models.user import User, BaseModel
import pycodestyle

class TestUser(unittest.TestCase):
    """Test for the User class"""

    @classmethod
    def setUpClass(cls):
        """Set up for Test"""
        cls.user = User()
        cls.user.first_name = 'Anwar'
        cls.user.last_name = 'Mamudu'
        cls.user.email = 'anwarsadat.d2@gmail.com'
        cls.user.password = 'Encrypted'

    @classmethod
    def tearDownClass(cls):
        """Tear down at end of Test"""
        del cls.user

    def tearDown(self):
        """ """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_pycodestyle_User(self):
        """Test pep8 compliance"""
        style_check = pycodestyle.StyleGuide(quiet=True)
        result = style_check.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, 'fix pycodestyle')

    def test_for_docstring(self):
        """Test for docstring"""
        self.assertIsNotNone(self.user.__doc__)

    def test_for_attributes(self):
        """Test if attributes are present in User dict"""
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)

    def test_is_subclass(self):
        """Test to see if User is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_attribute_type(self):
        """Test the attributes' types"""
        self.assertTrue(type(self.user.email), str)
        self.assertTrue(type(self.user.password), str)
        self.assertTrue(type(self.user.first_name), str)
        self.assertTrue(type(self.user.last_name), str)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE' == 'db'),
                    'This test should only execute got FileStorage')
    def test_save_User(self):
        """Test if the save method works"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict(self):
        """Test if dictionary works as it should"""
        self.assertTrue('to_dict' in dir(self.user), True)


if __name__ == "__main__":
    unittest.main()
