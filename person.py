# import car class here
from car import Car

class Person:

    def __init__(self, name, occupation):
        self._name = name
        self._occupation = occupation
        #if Car.owner == self.name:
        #    self._car_make = Car.make

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
    def car_year(self):
        return Car._year

    @car_year.getter
    def car_year(self, car_year):
        self._car_year = car_year

    # @property
    # def car_make(self):
    #     return self._car_make
    #
    # @car_make.getter
    # def car_make(self, car_make):
    #   self._car_make = car_make


    @classmethod
    def has_oldest_car(cls):
        oldest_owner = 'Bob'
        oldest_year = 2019
        for car in Car._all:
            if car.year < oldest_year:
                oldest_year = car.year
                oldest_owner = car.owner
            else: pass
        return oldest_owner

    @classmethod
    def drives_a(cls, make):
        return [car.owner for car in Car._all if car.make == make]

    def find_my_car(self):
        cars = Car.all()
        for car in cars:
            if car.owner == self:
                return car
        return "You don't have a car yet"

    def drives_same_make_as_me(self):
        cars = Car.all()
        my_car = self.find_my_car()
        same_cars = [car.owner for car in cars if car.owner != self and car.make == my_car.make]
        return same_cars

#    def drives_same_make_as_me(self):
#        return [car.owner for car in Car._all if car.make == self.car_make]
