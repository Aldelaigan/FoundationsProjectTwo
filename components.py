# CLASSES AND METHODS
class Store():
    def __init__(self, name):
        """
        Initializes a new store with a name.
        """
        self.name = name
        s1 = Store("Zara")
        s2 = Store("Nike")
        s3 = Store("Apple")
        s4 = Store("Pharmacy")
        # your code goes here!
        self.name = name
        self.products = []

    def add_product(self, product):
        """
        Adds a product to the list of products in this store.
        """
        self.products.append(product)
        
        # your code goes here!

    def print_products(self):
        """
        Prints all the products of this store in a nice readable format.
        """
        # your code goes here!
        print(%s: % self.name)
        for product in self.products:
            print(product)
            print()


class Product():
    def __init__(self, name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        # your code goes here!
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        # your code goes here!


class Cart():
    def __init__(self):
        """
        Initializes a new cart with an empty list of products.
        """
        self == 0
        # your code goes here!
        self.products = []

    def add_to_cart(self, product):
        """
        Adds a product to this cart.
        """
        self += self.append(product)# your code goes here!

    def get_total_price(self):
        """
        Returns the total price of all the products in this cart.
        """
        # your code goes here!
        for product in self.products:
            price += product.price


    def print_receipt(self):
        """
        Prints the receipt in a nice readable format.
        """
        # your code goes here!

    def checkout(self):
        """
        Does the checkout.
        """
        # your code goes here!
