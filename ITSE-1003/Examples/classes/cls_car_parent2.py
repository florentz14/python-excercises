# 1. CLASE PADRE (Parent Class)
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False

    def start_engine(self):
        self.is_running = True
        return f"El {self.brand} ha encendido su motor convencional."

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

# 2. CLASES HIJAS (Child Classes)


class SUV(Car):
    def __init__(self, brand, model, year, capacity=7):
        # super() conecta con el __init__ de Car
        super().__init__(brand, model, year)
        self.capacity = capacity

    def start_engine(self):
        return f"El SUV {self.brand} ruge con fuerza. Capacidad: {self.capacity} personas."


class SportsCar(Car):
    def __init__(self, brand, model, year, top_speed):
        super().__init__(brand, model, year)
        self.top_speed = top_speed

    def start_engine(self):
        return f"¡VROOOM! El {self.brand} deportivo está listo para correr a {self.top_speed} km/h."


class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_kwh):
        super().__init__(brand, model, year)
        self.battery_kwh = battery_kwh

    def start_engine(self):
        # Sobrescribimos el método: los eléctricos no rugen, hacen un zumbido
        return f"El {self.brand} {self.model} se activa en silencio... (Batería: {self.battery_kwh}kWh)"


class Truck(Car):
    def __init__(self, brand, model, year, load_capacity):
        super().__init__(brand, model, year)
        self.load_capacity = load_capacity

# --- Pruebas de Herencia ---


# Instanciamos diferentes objetos
mi_deportivo = SportsCar("Ferrari", "F8", 2024, 340)
mi_tesla = ElectricCar("Tesla", "Model S", 2025, 100)
mi_camion = Truck("Volvo", "FH16", 2023, "25 Toneladas")

# Probamos el polimorfismo (llamar al mismo método en diferentes objetos)
print(mi_deportivo.start_engine())
print(mi_tesla.start_engine())
# Este usa el método por defecto de la clase padre Car
print(mi_camion.start_engine())
print(mi_deportivo)
print(mi_tesla)
print(mi_camion)
