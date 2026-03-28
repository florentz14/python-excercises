class Car:
    def __init__(self, brand, model, gas):
        self.brand = brand
        self.model = model
        self.__gas = gas  # private attribute

    def show_gas(self):
        print("Gas level:", self.__gas, "gallons")

    def add_gas(self, amount):
        if amount > 0:
            self.__gas += amount
            print(amount, "gallons added")
        else:
            print("Invalid gas amount")


car1 = Car("Honda", "Civic", 2)

car1.show_gas()
car1.add_gas(3)
car1.show_gas()
car1.add_gas(-1)  # Invalid gas amount
car1.show_gas()
