from pydantic import BaseModel, Field

# 1. Definición de la Clase Padre (Parent Class)


class Car(BaseModel):
    brand: str
    model: str
    year: int = Field(
        gt=1885, description="Año de fabricación posterior al primer coche")

# 2. Definición de las Clases Hijas (Child Classes)


class SUV(Car):
    has_four_wheel_drive: bool = True
    seating_capacity: int = Field(default=5, ge=5)


class SportsCar(Car):
    top_speed: int = Field(..., description="Maximum speed in km/h")
    is_convertible: bool = False


class Truck(Car):
    cargo_capacity_kg: float
    number_of_axles: int = 2


class GolfCart(Car):
    is_electric: bool = True
    max_range_km: int = 40


class ElectricCar(Car):
    battery_capacity_kwh: float
    charging_time_hours: float


class LuxuryCar(Car):
    interior_material: str = "Leather"
    has_massage_seats: bool = True

# --- Ejemplo de implementación ---


# Creamos un coche eléctrico (hijo)
my_tesla = ElectricCar(
    brand="Tesla",
    model="Model 3",
    year=2024,
    battery_capacity_kwh=75.0,
    charging_time_hours=8.5
)

# Creamos un SUV (hijo)
my_suv = SUV(
    brand="Toyota",
    model="Land Cruiser",
    year=2023,
    seating_capacity=7
)

print(
    f"Coche Eléctrico: {my_tesla.brand} {my_tesla.model} (Batería: {my_tesla.battery_capacity_kwh}kWh)")
print(f"SUV: {my_suv.brand} {my_suv.model} (Capacidad: {my_suv.seating_capacity} personas)")
