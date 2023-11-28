from espresso import Espresso
from dark_roast import DarkRoast
from house_bland import HouseBlend
from mocha import Mocha
from soy import Soy
from whip import Whip


def main():
    beverage = Espresso()
    print(beverage.description + " $" + str(beverage.cost()))

    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(beverage2.description + " $" + str(beverage2.cost()))

    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(beverage3.description + " $" + str(beverage3.cost()))


if __name__ == "__main__":
    main()
