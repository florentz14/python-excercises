# -------------------------------------------------
# File Name: 49_product.py
# Author: Florentino Báez
# Date: 11_OOP
# Description: Simple Product class with name, price and info() method.
# -------------------------------------------------

class Product:
    """Class with attributes and a method."""
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return f"{self.name}: ${self.price:.2f}"

# Short list of products
products = [
    Product("Apple", 1.50),
    Product("Bread", 2.99),
    Product("Milk", 3.49),
]

# Usage
for p in products:
    print(p.info())
