import unittest
from unittest.mock import patch
from base_model import BaseModel  # Replace 'your_module' with the actual module name where BaseModel is defined
import datetime

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()

    def test_init_with_kwargs(self):
        kwargs = {
            'id': '123',
            'created_at': '2024-02-11T12:34:56.789',
            'updated_at': '2024-02-11T13:45:30.123',
            'name': 'example'
        }

        with patch('uuid.uuid4', return_value='123'):
            base_model = BaseModel(**kwargs)

        self.assertEqual(base_model.id, '123')
        self.assertEqual(base_model.created_at, datetime.datetime(2024, 2, 11, 12, 34, 56, 789000))
        self.assertEqual(base_model.updated_at, datetime.datetime(2024, 2, 11, 13, 45, 30, 123000))
        self.assertEqual(base_model.name, 'example')

    def test_init_without_kwargs(self):
        self.assertIsNotNone(self.base_model.id)
        self.assertIsNotNone(self.base_model.created_at)
        self.assertIsNotNone(self.base_model.updated_at)
        self.assertEqual(self.base_model.updated_at, self.base_model.created_at)

    def test_save_method(self):
        initial_updated_at = self.base_model.updated_at
        with patch('datetime.datetime.now', return_value=datetime.datetime(2024, 2, 11, 15, 30, 0)):
            self.base_model.save()

        self.assertNotEqual(self.base_model.updated_at, initial_updated_at)
        self.assertEqual(self.base_model.updated_at, datetime.datetime(2024, 2, 11, 15, 30, 0))

    def test_to_dict_method(self):
        obj_dict = self.base_model.to_dict()

        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], str(self.base_model.id))
        self.assertEqual(obj_dict['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], self.base_model.updated_at.isoformat())

    def test_str_method(self):
        str_representation = str(self.base_model)
        self.assertIn('BaseModel', str_representation)
        self.assertIn(str(self.base_model.id), str_representation)

if __name__ == '__main__':
    unittest.main()

