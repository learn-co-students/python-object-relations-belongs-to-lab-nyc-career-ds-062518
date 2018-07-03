class Car:

    _all = []

    @classmethod
    def all(cls):
        return cls._all
    @classmethod
    def cars_driven_by(cls, occupation):
        return [car for car in cls.all() if car.owner.occupation == occupation]

    def __init__(self, make, model, year, owner):
        self._make = make
        self._model = model
        self._year = year
        self._owner = owner
        Car._all.append(self)

    @property
    def make(self):
        return self._make
    @property
    def model(self):
        return self._model
    @property
    def year(self):
        return self._year
    @property
    def owner(self):
        return self._owner
    @owner.setter
    def owner(self, owner):
        self._owner = owner
