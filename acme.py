import random


class Product:
    """
    Product of Acme Corporation
    """
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        """
        Method to determine if product is stealable
        """
        ratio = self.price/self.weight
        if ratio < 0.5:
            return "Not so stealable"
        elif all([ratio >= 0.5, ratio < 1]):
            return "Kinda stealable"
        else:
            return "Very stealable!"

    def explode(self):
        """
        Method to determine if product will explode
        """
        flammable = self.flammability * self.weight
        if flammable < 10:
            return "...fizzle"
        elif all([flammable >= 10, flammable < 50]):
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    """
    Glove Product of Acme Corporation
    """

    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        """
        Method to determine if the product explode
        """
        return "...it's a glove."

    def punch(self):
        """
        Method to determine punch power
        """
        weight = self.weight
        if weight < 5:
            return "That tickles."
        elif all([weight >= 5, weight < 15]):
            return "Hey that hurt!"
        else:
            return "OUCH!"
