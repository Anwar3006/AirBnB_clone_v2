#!/usr/bin/python3
""" """
from models.city import City
import pycodestyle
import os
import unittest
from models.base_model import BaseModel

class Test_City(unittest.TestCase):
    """ """
    @classmethod
    def setUpClass(cls):
        """ """
        cls.city = City()
        cls.city.name = ''
        cls.city.places = ''
        cls.city.state_id = ''

    @classmethod
    def tearDownClass(cls):
        """ """
        del cls.city

    def tearDown(self):
        """ """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_pycodestyle_City(self):
        """ """
        style_guide = pycodestyle.StyleGuide(quiet=True)
        result = style_guide.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, 'Fix code')

    def test_for_doc(self):
        """ """
        self.assertIsNotNone(self.city.__doc__)

    def test_for_attributes(self):
        """ """
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)
        self.assertTrue('places' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)

    def test_for_subclass(self):
        """ """
        self.assertEqual(issubclass(self.city.__class__, BaseModel), True)

    def test_attributes_type(self):
        """ """
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.places), str)
        self.assertEqual(type(self.city.state_id), str)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE' == 'db'),
                    'Test to be excuted only for FileStorage')
    def test_to_save(self):
        """ """
        self.city.save()
        self.assertEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict(self):
        """ """
        self.assertEqual('to_dict' in dir(self.city), True)

if __name__ == "__main__":
    unittest.main()