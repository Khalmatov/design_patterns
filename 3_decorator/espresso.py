from beverage import Beverage


class Espresso(Beverage):
    _description = 'Espresso'

    def cost(self):
        return 1.99
