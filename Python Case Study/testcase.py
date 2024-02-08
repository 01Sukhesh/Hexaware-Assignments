import sys
import mysql.connector
import unittest
from Entity import products
from serviceprovider import serviceprovider



class TestEcommerceSystem(unittest.TestCase):
    def setUp(self):
        self.ecommerce = serviceprovider()

    def test_create_product(self):
        product_id = 108
        name="lemon pickle"
        price=8
        description='quality lemon pickle'
        stockQuantity=60
        created_product =self.ecommerce.create_product(product_id, name, price,description,stockQuantity)
        self.assertTrue(created_product)

    def test_add_to_cart(self):
        cart_id = 17
        customer_id = 2
        product_id = 2
        quantity = 4
        added_to_cart = self.ecommerce.addTocart(cart_id ,customer_id, product_id, quantity)
        self.assertTrue(added_to_cart)