class Car:
    def __init__(self, model, fuel_capacity):
        self.model = model
        self.fuel_capacity = fuel_capacity
        self.current_fuel = 0
    def refuel(self, amount):
        if self.current_fuel + amount > self.fuel_capacity:
            raise Exception("Бак переполнен")
        self.current_fuel += amount
    def drive(self, distance):
        fuel_needed = distance * 8 / 100
        if self.current_fuel < fuel_needed:
            raise Exception("Недостаточно топлива")
        self.current_fuel -= fuel_needed
