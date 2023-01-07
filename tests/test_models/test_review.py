#!/usr/bin/python3
""" """
import unittest
import os
from models.base_model import BaseModel
from models.review import Review
import pycodestyle

class Test_Review(unittest.TestCase):
    """ """

    @classmethod
    def setUpClass(cls):
        """Set Up class for Testing"""
        cls.reviews = Review()
        cls.reviews.text = 'Positive reviews from User_1'
        cls.reviews.place_id = 'Place_id of User_1'
        cls.reviews.user_id = 'User_id of User_1'

    @classmethod
    def tearDownClass(cls):
        """ """
        del cls.reviews

    def tearDown(self):
        """ """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_pycodestyle_Review(self):
        """ """
        style_guide = pycodestyle.StyleGuide(quiet=True)
        result = style_guide.check_files(['models/review.py'])
        self.assertTrue(result.total_errors, 0, "Fix Pycodestyle")

    def test_for_doc(self):
        """ """
        self.assertIsNotNone(self.reviews.__doc__)

    def test_for_attributes(self):
        """ """
        self.assertTrue('place_id' in self.reviews.__dict__)
        self.assertTrue('user_id' in self.reviews.__dict__)
        self.assertTrue('text' in self.reviews.__dict__)
        self.assertTrue('id' in self.reviews.__dict__)

    def test_for_subclass(self):
        """ """
        self.assertTrue(issubclass(self.reviews.__class__, BaseModel), True)

    def test_attribute_type(self):
        """ """
        self.assertTrue(type(self.reviews.place_id), str)
        self.assertTrue(type(self.reviews.user_id), str)
        self.assertTrue(type(self.reviews.text), str)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE' == 'db'),
                    'Test is only executed for FileStorage')
    def test_save_Review(self):
        """ """
        self.reviews.save()
        self.assertNotEqual(self.reviews.created_at, self.reviews.updated_at)

    def test_to_dict(self):
        """ """
        self.assertTrue('to_dict' in dir(self.reviews), True)

if __name__ == "__main__":
    unittest.main()