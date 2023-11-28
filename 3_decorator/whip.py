from condiment_decorator import CondimentDecorator


class Whip(CondimentDecorator):

    def __init__(self, beverage):
        self.beverage = beverage

    @property
    def description(self):
        return self.beverage.description + ", Whip"

    def cost(self):
        return self.beverage.cost() + 0.10
