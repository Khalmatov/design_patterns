from abc import ABC

from beverage import Beverage
from enums import Size


class CondimentDecorator(Beverage, ABC):
    beverage: Beverage

    @property
    def size(self) -> Size:
        return self.beverage.size
