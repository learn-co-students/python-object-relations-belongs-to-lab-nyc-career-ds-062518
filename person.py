# import car class here
from car import Car
class Person:
    def __init__(self, name, occupation):
        self._name = name
        self._occupation = occupation
    @property
    def name (self):
        return self._name
    @property
    def occupation(self):
        return self._occupation
    @property
    def car_year (self):
        return Car.year
    @classmethod
    def has_oldest_car(cls, Otherclass=Car):
        cars = Car.all()
        oldestcar= cars[0]
        for car in cars:
            if car.year < oldestcar.year:
                oldestcar= car
        return oldestcar.owner
    @classmethod
    def drives_a (cls, make):
        return [car.owner for car in Car.all() if car.make == make]
    def find_my_car(self):
        for car in Car.all():
            if car.owner== self:
                return car
            else:
                "no car"
    def drives_same_make_as_me(self):
        my_car_make = self.find_my_car().make
        drives_the_same_car = [car.owner for car in Car.all() if car.owner != self and car.make == my_car_make]
        return drives_the_same_car
