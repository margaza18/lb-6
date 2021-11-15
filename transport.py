from abc import ABCMeta, abstractmethod, abstractproperty, ABC


class Car:
    __metaclass__ = ABCMeta

    def __init__(self, car_type: str, car_cost: str, car_speed: int, car_year: int):
        self.car_type = car_type
        self.cost = car_cost
        self.speed = car_speed
        self.year = car_year

    @property
    @abstractmethod
    def height(self, x: int, y: int, z: int):
        print(self.car_type)
        print(x, y, z)

    @property
    @abstractmethod
    def passengers_count(self, count: int):
        print(self.car_type)
print(count)

    @property
    @abstractmethod
    def home_port(self, port: str):
        print(self.car_type)
        print(port)


class Aircraft(Car, ABC):

    def height(self, x, y, z):
        print(self.car_type)
        print(x, y, z)

    def passengers_count(self, count):
        print(self.car_type)
        print(count)


class Ship(Car, ABC):
    def passengers_count(self, count):
        print(self.car_type)
        print(count)

    def home_port(self, port):
        print(self.car_type)
        print(port)


aircraft = Aircraft("Flick", "1202", 1200, 1000)
aircraft.height(1, 2, 3)
