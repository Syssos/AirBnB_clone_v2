#!/usr/bin/python3
'''
All the test for the base_model are implemented here.
'''
import unittest
from models.base_model import BaseModel
from io import StringIO
import sys
import datetime
import models


class TestBase(unittest.TestCase):
    '''
    Testing the base class model.
    '''
    @classmethod
    
    def setUpClass(cls):
        '''
        Initializing instance for class
        '''
        cls.my_model = BaseModel()
        cls.my_model.name = "Cody"
        

    def test_id_type(self):
        '''
        Checks that the type of the id is string.
        '''
        self.assertEqual("<class 'str'>", str(type(self.my_model.id)))
        
    def test_ids_differ(self):
        '''
        Checks that the ids between two instances are different.
        '''
        meow_model = BaseModel()
        self.assertNotEqual(self.my_model.id, meow_model.id)

    def test_name(self):
        '''
        Checks that an attribute can be added.
        '''
        self.assertEqual("Cody", self.my_model.name)
    
    def test_a_updated_created_equal(self):
        '''
        Checks that both dates are equal.
        '''
        self.assertEqual(self.my_model.updated_at.year,
                         self.my_model.created_at.year)

    def test_instance_diff(self):
        '''
        Test that the my_model and new_model are
        not the same instance.
        '''
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(my_model_dict)
        self.assertNotEqual(self.my_model, new_model)
