class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0  # new property

    def accelerate(self):
        self.speed += 10  # increase by 10

    def brake(self):
        if self.speed >= 10:
            self.speed -= 10  # decrease by 10
        else:
            self.speed = 0

    def display_speed(self):
        print("Speed:", self.speed)

    # NEW METHOD
    def check_gas(self, gallons):
        if gallons < 1:
            print("Gas tank almost empty")
        elif gallons > 3:
            print("Gas tank is filled")
        else:
            print("Gas tank is ok")


# create the objects
florentinoCar = Car("Ford", "Mustang", 2025)

florentinoCar.check_gas(0.5)
florentinoCar.check_gas(2)
florentinoCar.check_gas(5)
florentinoCar.accelerate()
florentinoCar.display_speed()
florentinoCar.accelerate()
florentinoCar.display_speed()
florentinoCar.accelerate()
florentinoCar.brake()
florentinoCar.display_speed()
florentinoCar.accelerate()
florentinoCar.display_speed()
