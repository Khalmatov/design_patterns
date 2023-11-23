from abc import ABC, abstractmethod


class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        """Реализация полета"""


class FlyWithWings(FlyBehavior):
    def fly(self):
        """Реализация полета для всех летающих уток"""
        print("I'm flying!!")


class FlyNoWay(FlyBehavior):
    def fly(self):
        """Реализация полета уток, которые летать не умеют"""
        print("I can't fly")


class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        """Реализация кряканья"""


class Quack(QuackBehavior):
    def quack(self):
        """Утки, которые крякают"""
        print("Quack")


class Squack(QuackBehavior):
    def quack(self):
        """Утки, которые пищат"""
        print("Squack")


class MuteQuack(QuackBehavior):
    def quack(self):
        """Утки, которые не издают звуков"""
        print("<< Silence >>")


class Duck:
    fly_behavior: FlyBehavior
    quack_behavior: QuackBehavior

    def perform_quack(self):
        self.quack_behavior.quack()

    def perform_fly(self):
        self.fly_behavior.fly()

    def swim(self):
        print('All ducks float, even decoys!')

    def display(self):
        pass

    def set_fly_behavior(self, fb: FlyBehavior):
        self.fly_behavior = fb

    def set_quack_behavior(self, qb: QuackBehavior):
        self.quack_behavior = qb


class MallardDuck(Duck):

    def __init__(self):
        self.quack_behavior = Quack()
        self.fly_behavior = FlyWithWings()

    def display(self):
        print("I'm a real Mallard duck")


def main():
    mallard: Duck = MallardDuck()
    mallard.perform_quack()
    mallard.perform_fly()
    mallard.set_fly_behavior(FlyNoWay())
    mallard.perform_fly()


if __name__ == '__main__':
    main()
