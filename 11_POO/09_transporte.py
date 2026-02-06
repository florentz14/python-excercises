# Ejemplo de Clases: Transporte
# Este programa demuestra la herencia y polimorfismo con diferentes tipos de transporte

# Clase padre: Transporte
class Transporte:
    """Clase base para todos los tipos de transporte"""

    def __init__(self, marca, modelo, año):
        """Constructor para inicializar los atributos básicos"""
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def describir(self):
        """Método para describir el transporte"""
        return f"{self.marca} {self.modelo} ({self.año})"

    def moverse(self):
        """Método virtual que será sobrescrito en las clases derivadas"""
        return "El transporte se está moviendo"


# Clase derivada: Automóvil
class Automovil(Transporte):
    """Clase que representa un automóvil"""

    def __init__(self, marca, modelo, año, puertas):
        """Constructor que llama al constructor de la clase padre"""
        super().__init__(marca, modelo, año)
        self.puertas = puertas

    def describir(self):
        """Sobrescribe el método describir de la clase padre"""
        return f"Automóvil: {super().describir()} - {self.puertas} puertas"

    def moverse(self):
        """Sobrescribe el método moverse de la clase padre"""
        return f"El automóvil {self.marca} se está moviendo por la carretera"


# Clase derivada: Motocicleta
class Motocicleta(Transporte):
    """Clase que representa una motocicleta"""

    def __init__(self, marca, modelo, año, cilindrada):
        """Constructor que llama al constructor de la clase padre"""
        super().__init__(marca, modelo, año)
        self.cilindrada = cilindrada

    def describir(self):
        """Sobrescribe el método describir de la clase padre"""
        return f"Motocicleta: {super().describir()} - {self.cilindrada}cc"

    def moverse(self):
        """Sobrescribe el método moverse de la clase padre"""
        return f"La motocicleta {self.marca} se está moviendo a toda velocidad"


# Clase derivada: Bicicleta
class Bicicleta(Transporte):
    """Clase que representa una bicicleta"""

    def __init__(self, marca, modelo, año, tipo_cambios):
        """Constructor que llama al constructor de la clase padre"""
        super().__init__(marca, modelo, año)
        self.tipo_cambios = tipo_cambios

    def describir(self):
        """Sobrescribe el método describir de la clase padre"""
        return f"Bicicleta: {super().describir()} - {self.tipo_cambios} cambios"

    def moverse(self):
        """Sobrescribe el método moverse de la clase padre"""
        return f"La bicicleta {self.marca} se está moviendo pedaleando"


# Clase derivada: Avión
class Avion(Transporte):
    """Clase que representa un avión"""

    def __init__(self, marca, modelo, año, capacidad_pasajeros):
        """Constructor que llama al constructor de la clase padre"""
        super().__init__(marca, modelo, año)
        self.capacidad_pasajeros = capacidad_pasajeros

    def describir(self):
        """Sobrescribe el método describir de la clase padre"""
        return f"Avión: {super().describir()} - {self.capacidad_pasajeros} pasajeros"

    def moverse(self):
        """Sobrescribe el método moverse de la clase padre"""
        return f"El avión {self.marca} está volando en el cielo"


# PROGRAMA PRINCIPAL
print("=" * 60)
print("EJEMPLO DE CLASES: TRANSPORTE Y SUS TIPOS")
print("=" * 60)

# Crear diferentes tipos de transporte
auto = Automovil("Toyota", "Corolla", 2023, 4)
moto = Motocicleta("Yamaha", "YZF-R3", 2022, 321)
bici = Bicicleta("Trek", "FX 3", 2021, 21)
avion = Avion("Boeing", "787 Dreamliner", 2020, 242)

# Lista de transportes
transportes = [auto, moto, bici, avion]

# Mostrar información de cada transporte
print("\nInformación de los transportes:")
print("-" * 60)
for transporte in transportes:
    print(f"✓ {transporte.describir()}")

# Demostrar polimorfismo (mismo método, diferentes comportamientos)
print("\nDemostrando movimiento (Polimorfismo):")
print("-" * 60)
for transporte in transportes:
    print(f"→ {transporte.moverse()}")

# Crear más transportes
print("\n" + "=" * 60)
print("Creando más transportes:")
print("=" * 60)

auto2 = Automovil("Mercedes", "C-Class", 2024, 2)
moto2 = Motocicleta("Harley-Davidson", "Street 750", 2023, 750)

transportes_adicionales = [auto2, moto2]

for transporte in transportes_adicionales:
    print(f"✓ {transporte.describir()}")
    print(f"  {transporte.moverse()}\n")
