# import car class here
from car import Car

class Person:

    # _all = []

    def __init__(self, name, occupation):
        self._name = name
        self._occupation = occupation
        # Person._all.append(self)

    # @classmethod
    # def all(cls):
    #     return cls._all

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
        return Car.has_oldest_car(cls)

    @classmethod
    def drives_a(cls, make):
        return Car.drives_a(cls, make)

    def drives_same_make_as_me(self):
        #find make associated with instance
        make = Car.return_make(self)
        owner_list = Person.drives_a(make)
        owner_list.remove(self)
        return owner_list

    # @classmethod
    # def cars_driven_by(cls, OtherClass, occupation):
    #     return [person for person in cls._all if person._occupation == occupation]
