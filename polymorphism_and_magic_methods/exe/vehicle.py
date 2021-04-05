from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass

    def can_be_driven(self, distance, multiplyer):
        return self.fuel_quantity > (self.fuel_consumption + multiplyer) * distance


class Car(Vehicle):
    SUMMER_FUEL_INCREASE = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        if not self.can_be_driven(distance, self.SUMMER_FUEL_INCREASE):
            return
        self.fuel_quantity -= (self.fuel_consumption + self.SUMMER_FUEL_INCREASE) * distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    SUMMER_FUEL_INCREASE = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        if not self.can_be_driven(distance, self.SUMMER_FUEL_INCREASE):
            return
        self.fuel_quantity -= (self.fuel_consumption + self.SUMMER_FUEL_INCREASE) * distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)