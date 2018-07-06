
from car import Car

class Person:

    def __init__(self, name, occupation):
        self._name = name
        self._occupation = occupation

    @property
    def name (self):
        return self._name

    @name.setter
    def name (self,name):
        self._name = name

    @property
    def occupation (self):
        return self._occupation

    @occupation.setter
    def occupation(self, occupation):
        self._occupation = occupation

    def car(cls):
        return cls.all

    @classmethod
    def has_oldest_car(cls):
        cars = Car.all()
        oldest = cars[0]
        for car in cars:
            if car.year< oldest.year:
                oldest = car
        return oldest.owner

    @classmethod
    def drives_a (cls, make):
        owners = [car.owner for car in Car.all() if car.make == make]
        return owners

    def find_car (self):
        cars = Car.all()
        for car in cars:
            if car.owner == self:
                return car

    def drives_same_make_as_me(self):
        cars = Car.all()
        mycar = self.find_car()
        same_cars = [car.owner for car in cars if car.owner != self and car.make == mycar.make]
        return same_cars
