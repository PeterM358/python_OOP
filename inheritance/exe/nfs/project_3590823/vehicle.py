class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, value):
        self.__fuel = value

    @property
    def horse_power(self):
        return self.__horse_power

    @horse_power.setter
    def horse_power(self, value):
        self.__horse_power = value

    def drive(self, kilometers):
        if self.fuel >= kilometers * self.fuel_consumption:
            self.fuel -= kilometers * self.fuel_consumption


