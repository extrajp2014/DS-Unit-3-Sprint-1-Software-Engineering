from random import randint, sample, uniform
from acme import Product

adjectives = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
nouns = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    """
    Generate list of products for Acme Corporation
    """
    products = []
    for i in range(0, num_products):
        name = adjectives[randint(0, len(adjectives)-1)] + \
               " " + nouns[randint(0, len(nouns)-1)]
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0.0, 2.5)
        product = Product(name, price, weight, flammability)
        products.append(product)
    return products


def inventory_report(products):
    """
    print inventory report of Acme Corporation products
    """
    products_name = [i.name for i in products]
    products_price = [i.price for i in products]
    products_weight = [i.weight for i in products]
    products_flammability = [i.flammability for i in products]
    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print("Unique product names:", len(set(products_name)))
    print("Average price:", sum(products_price)/len(products_price))
    print("Average weight:", sum(products_weight)/len(products_weight))
    print("Average flammability:",
          sum(products_flammability)/len(products_flammability))

if __name__ == '__main__':
    inventory_report(generate_products())
