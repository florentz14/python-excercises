class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fuel_type(self):
        print("This car uses regular fuel")


class ElectricCar(Car):
    def fuel_type(self):  # override method fuel_type
        print("This car uses electricity")


class HybridCar(Car):
    def fuel_type(self):  # polymorphism
        print("This car uses gas and electricity")


car1 = Car("Toyota", "Corolla")
car2 = ElectricCar("Tesla", "Model S")
car3 = HybridCar("Toyota", "Prius")

car1.fuel_type()  # this car uses regular fuel
car2.fuel_type()  # this car uses electricity
car3.fuel_type()  # this car uses gas and electricity
