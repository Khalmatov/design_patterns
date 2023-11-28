from abc import ABC, abstractmethod

from enums import Size


class Beverage(ABC):
    _size: Size = Size.TALL
    _description: str = 'Unknown Beverage'

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description: str):
        self._description = description

    @property
    def size(self) -> Size:
        return self._size

    @size.setter
    def size(self, size: Size):
        self._size = size

    @abstractmethod
    def cost(self):
        pass
