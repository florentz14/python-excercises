class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print(self.brand, self.model, "engine started")
# parent class Car finishes here

# FIRST CHILD CLASS


class ElectricCar(Car):  # INHERIT ALL FROM CAR(PROPERTIES#AND METHODS)

    def charge_battery(self):
        print(self.brand, self.model, "is charging")

#### THISISTHEENDOFCHILDCLASS-ELECTRICCAR#########


class Truck(Car):  # WE CREATE SECOND CHILD TRUCK
    def load_cargo(self):  # NEW METHOD ONLY FOR
        print(self.brand, self.model, "is loading cargo")


# create an object
titusCar = ElectricCar("MumboJumbo", "Model 3", 2027)
titusCar.start_engine()  # this is from Car
titusCar.charge_battery()  # this is from child class ElectricCar

# create another object
christinaTruck = Truck("TOYOTA", "TACOMA", 2002)
christinaTruck.start_engine()  # coming from parent class
christinaTruck.load_cargo()  # coming from child class
