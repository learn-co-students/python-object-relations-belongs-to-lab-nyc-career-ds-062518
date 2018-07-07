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
    def name(self,name):
        self._name = name

    @property
    def occupation(self):
        return self._occupation

    @occupation.setter
    def occupation(self, occupation):
        self._occupation = occupation

    @classmethod
    def has_oldest_car(cls):
        car_year_list = [car._year for car in Car.all()]
        oldest = min(car_year_list)
        return [car._owner for car in Car.all() if car._year == oldest][0]

    @classmethod
    def drives_a(cls, car_make):
        return [car.owner for car in Car.all() if car._make == car_make]

    def find_my_car(self):
        return[car.make for car in Car.all() if car.owner == self][0]

    def drives_same_make_as_me(self):
        return [car.owner for car in Car.all() if car.make == self.find_my_car() and car.owner != self]
