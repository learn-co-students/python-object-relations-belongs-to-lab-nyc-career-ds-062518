
from car import Car

class Person:

    def __init__(self, name, occupation):
        self._name = name
        self._occupation = occupation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def occupation(self):
        return self._occupation

    @occupation.setter
    def occupation(self, occupation):
        self._occupation = occupation

    @classmethod
    def has_oldest_car(cls):
        oldcar = min(Car.all(), key = lambda car: car._year)
        return oldcar._owner

    @classmethod
    def drives_a(cls, make):
        return [car._owner for car in Car.all() if car._make == make]

    def drives_same_make_as_me(self):
        mymake = [car._make for car in Car.all() if car._owner == self][0]
        return [car._owner for car in Car.all() if car._make == mymake and car._owner != self]
