from beverage import Beverage


class HouseBlend(Beverage):
    _description = 'House Blend Coffee'

    def cost(self):
        return 0.89
