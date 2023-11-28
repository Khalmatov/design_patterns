from beverage import Beverage


class Decaf(Beverage):
    _description = 'Decaf Coffee'

    def cost(self):
        return 1.05
