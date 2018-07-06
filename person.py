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

    @property
    def car(self):
        return [person for person in Car.all() if person.owner == self]

    @classmethod
    def has_oldest_car(cls):
        car_years = [yr.year for yr in Car.all()]
        oldest_car = [old.owner for old in Car.all() if min(car_years) == old.year]
        return oldest_car[0]

    @classmethod
    def drives_a(cls, car):
        return [worker.owner for worker in Car.all() if worker.make == car]


    def drives_same_make_as_me(self):
        same_car = [type.owner for type in Car.all() if type.make == self.car[0].make]
        return [type for type in same_car if type != self]

    # @classmethod
    # def cars_driven_by(cls, job):
    #     same_car = []
    #     for type in Car.all():
    #         if type.owner.occupation == job:
    #             same_car.append(type)
    #     return same_car
#     return [type.owner for type in Car.all() if type.owner.occupation == job]
#
