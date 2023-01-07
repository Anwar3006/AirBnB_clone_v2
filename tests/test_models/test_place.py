#!/usr/bin/python3
""" """
import os
import pycodestyle
import unittest
from models.base_model import BaseModel
from models.place import Place


class Test_Place(unittest.TestCase):
    """ """

    @classmethod
    def setUpClass(cls):
        """ """
        cls.place = Place()
        cls.place.city_id = 'New Britain'
        cls.place.user_id = 'User_id of User_1'
        cls.place.name = 'Name of Place'
        cls.place.description = 'Description of Place'
        cls.place.number_rooms = 6
        cls.place.number_bathrooms = 4
        cls.place.max_guest = 20
        cls.place.price_by_night = 79
        cls.place.latitude = 56.65
        cls.place.longitude = 134.45

    @classmethod
    def tearDownClass(cls):
        """ """
        del cls.place

    def tearDown(self):
        """ """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_pycodestyle_Place(self):
        """ """
        style_guide = pycodestyle.StyleGuide(quiet=True)
        result = style_guide.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0, 'Fix errors')

    def test_for_doc(self):
        """ """
        self.assertIsNone(self.place.__doc__)

    def test_for_attributes(self):
        """ """
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('number_of_rooms' in self.place.__dict__)
        self.assertTrue('description' in self.place.__dict__)
        self.assertTrue('number_of_bathrooms' in self.place.__dict__)
        self.assertTrue('max_guest' in self.place.__dict__)
        self.assertTrue('price_by_night' in self.place.__dict__)
        self.assertTrue('latitude' in self.place.__dict__)
        self.assertTrue('longitude' in self.place.__dict__)

    def test_for_subclass(self):
        """ """
        self.assertEqual(issubclass(self.place.__class__, BaseModel), True)

    def test_attributes_type(self):
        """ """
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE' == 'db'),
                    'Test to execute only for FileStorage')
    def test_save_Place(self):
        """ """
        self.assertEqual(self.place.created_at, self.place.updated_at)

    def test_to_dict(self):
        """ """
        self.assertEqual('to_dict' in dir(self.place), True)


if __name__ == "__main__":
    unittest.main()
    