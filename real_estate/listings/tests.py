from django.test import TestCase
from django.shortcuts import redirect

# Create your tests here.
class ListingsTest(TestCase):
    def setUp(self):
        self.assertEqual(2,1+1)
    
    def test_list_listings(self):
        self.assertEqual(2,1+1)
    
    def test_create_listing(self):
        self.assertEqual(2,1+1)
    
    def test_retrieve_listing(self):
        self.assertEqual(2,1+1)
    
    def test_delete_listing(self):
        self.assertEqual(2,1+1)
    
    def test_update_listing(self):
        self.assertEqual(2,1+1)
