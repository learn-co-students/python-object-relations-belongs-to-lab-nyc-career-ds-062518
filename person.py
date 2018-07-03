# import car class here
from car import Car

class Person:
    _all = []

    @classmethod
    def all(cls):
        return cls._all
#Is it a problem that I dont call any class variables from Person in this class method??
    @classmethod
    def has_oldest_car(cls):
        car_year_list = [car.year for car in Car.all()]
        car_year_list_min = min(car_year_list)
        return [car.owner for car in Car.all() if car.year == car_year_list_min][0]
#Assuming person objects only have one car.
    @classmethod
    def drives_a(cls, make):
        return [person for person in cls.all() if person.car[0].make == make]


    def __init__(self, name, occupation):
        self._name = name
        self._occupation = occupation
        Person.all().append(self)

    @property
    def name(self):
        return self._name
    @property
    def occupation(self):
        return self._occupation
    @property
    def car(self):
        return [car for car in Car.all() if car.owner == self]

    def drives_same_make_as_me(self):
        return [person for person in Person.all() if (self.car[0].make == person.car[0].make and self != person)]
