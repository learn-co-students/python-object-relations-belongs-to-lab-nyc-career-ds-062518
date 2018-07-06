class Car:

    _all = []

    def __init__(self, make, model, year, owner):
        self._make = make
        self._model = model
        self._year = year
        self._owner = owner
        Car._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

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
    def cars_driven_by(cls, job):
        same_car = []
        for type in cls.all():
            if type.owner.occupation == job:
                same_car.append(type)
        return same_car
#     return [type.owner for type in Car.all() if type.owner.occupation == job]
#
