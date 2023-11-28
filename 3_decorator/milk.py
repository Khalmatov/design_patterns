from condiment_decorator import CondimentDecorator


class Milk(CondimentDecorator):

    def __init__(self, beverage):
        self.beverage = beverage

    def cost(self):
        return self.beverage.cost() + 0.10
