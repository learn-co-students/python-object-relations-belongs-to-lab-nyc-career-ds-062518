# import car class here
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
        return Car.oldest_car(cls)

    @classmethod
    def drives_a(cls, make):
        return Car.make_owner(cls, make)

    def drives_same_make_as_me(self):
        make = Car.return_make(self)
        owner_list = Person.drives_a(make)
        owner_list.remove(self)
        return owner_list
