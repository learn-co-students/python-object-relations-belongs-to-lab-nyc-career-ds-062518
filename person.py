# import car class here
from car import Car

class Person:

    _all  = []

    def __init__(self, name, occupation):
        self._name = name
        self._occupation = occupation
        Person._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def has_oldest_car(cls):
        oldest = 3000
        car_owner_name = 'Bob'
        for car in Car._all:
            if not car.year < oldest:
                continue
            else:
                oldest = car.year
                car_owner_name = car.owner
        return car_owner_name

    @classmethod
    def drives_a(cls, make):
        has_car_list = []
        for car in Car.all():
            if make == car.make:
                has_car_list.append(car.owner)
        return has_car_list

    def drives_same_make_as_me(self):
        car_make_local = None
        for car in Car.all():
            if not self == car.owner:
                continue
            else:
                car_make_local = car.make
        drives_same = [item for item in Person.drives_a(car_make_local)]
        drives_same.remove(self)
        return drives_same



    #decorator for _name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    #decorator for _occupation

    @property
    def occupation(self):
        return self._occupation

    @occupation.setter
    def occupation(self, occupation):
        self._occupation = occupation
