from base import Vehicle
from exceptions import CargoOverload

class Plane(Vehicle):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0, max_cargo=0):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, weight):
        if self.cargo + weight > self.max_cargo:
            raise CargoOverload("Cargo overload")
        self.cargo += weight

    def remove_all_cargo(self):
        previous = self.cargo
        self.cargo = 0
        return previous
