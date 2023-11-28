from condiment_decorator import CondimentDecorator

from enums import Size


class Soy(CondimentDecorator):

    def __init__(self, beverage):
        self.beverage = beverage

    @property
    def description(self):
        return self.beverage.description + ", Soy"

    def cost(self):
        cost = self.beverage.cost()
        if self.beverage.size == Size.TALL:
            cost += 0.10
        elif self.beverage.size == Size.GRANDE:
            cost += 0.15
        elif self.beverage.size == Size.VENTI:
            cost += 0.20
        return cost
