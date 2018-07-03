class Car:

    _all = []

    def __init__(self, make, model, year, owner):
        self._make = make
        self._model = model
        self._year = year
        self._owner = owner
        Car._all.append(self)

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, make):
        self._make = make

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        self._year = year

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        self._owner = owner

    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def oldest_car(cls, OtherClass):
        car_year_min = min([car.year for car in cls._all])
        return [car.owner for car in cls._all if car.year == car_year_min][0]

    @classmethod
    def make_owner(cls, OtherClass, make):
        return [car.owner for car in cls._all if car.make == make]

    @classmethod
    def return_make(cls, owner):
        return [car.make for car in cls._all if car.owner == owner][0]

    @classmethod
    def cars_driven_by(cls, occupation):
        return [car for car in cls._all if car.owner.occupation == occupation]
