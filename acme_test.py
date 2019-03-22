#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, adjectives, nouns


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_flammability(self):
        """Test default product flammability being 0.5"""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)

    def test_product_method_stealability(self):
        """Test stealability method """
        prod = Product('Test Product', price=1, weight=3)
        self.assertEqual(prod.stealability(), "Not so stealable")
        prod = Product('Test Product', price=2, weight=1)
        self.assertEqual(prod.stealability(), "Very stealable!")

    def test_product_method_explode(self):
        """Test explode method """
        prod = Product('Test Product', weight=3, flammability=1)
        self.assertEqual(prod.explode(), "...fizzle")
        prod = Product('Test Product', weight=60, flammability=1)
        self.assertEqual(prod.explode(), "...BABOOM!!")


class AcmeReportTests(unittest.TestCase):
    """Making sure Acme Report is correct!"""
    def test_default_num_products(self):
        """Test default product list size is 30"""
        prod = generate_products()
        self.assertEqual(len(prod), 30)

    def test_legal_names(self):
        """Test products have valid names"""
        products_name = [i.name for i in generate_products()]
        all_words = adjectives + nouns
        for name in products_name:
            self.assertIn(name.split()[0], all_words)
            self.assertIn(name.split()[1], all_words)

if __name__ == '__main__':
    unittest.main()
