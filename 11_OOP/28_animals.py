# Ejemplo de Clases: Animales
# Este programa demuestra la herencia y polimorfismo con diferentes tipos de animales


class Animal:
    """Clase base para todos los tipos de animales"""

    def __init__(self, nombre: str, edad: int, especie: str) -> None:
        """Constructor para inicializar los atributos básicos"""
        self.nombre = nombre
        self.edad = edad
        self.especie = especie

    def describir(self) -> str:
        """Método para describir el animal"""
        return f"{self.nombre} es un {self.especie} de {self.edad} años"

    def hacer_sonido(self) -> str:
        """Método virtual que será sobrescrito en las clases derivadas"""
        return f"{self.nombre} hace un sonido"

    def moverse(self) -> str:
        """Método para el movimiento del animal"""
        return f"{self.nombre} se está moviendo"


class Perro(Animal):
    """Clase que representa un perro"""

    def __init__(self, nombre: str, edad: int, raza: str) -> None:
        """Constructor que llama al constructor de la clase padre"""
        super().__init__(nombre, edad, "Perro")
        self.raza = raza

    def describir(self):
        """Sobrescribe el método describir de la clase padre"""
        return f"{super().describir()} - Raza: {self.raza}"

    def hacer_sonido(self):
        """Sobrescribe el método hacer_sonido de la clase padre"""
        return f"{self.nombre} ladra: ¡Guau guau!"

    def moverse(self):
        """Sobrescribe el método moverse de la clase padre"""
        return f"{self.nombre} está corriendo felizmente"

    def traer_objeto(self):
        """Método específico de la clase Perro"""
        return f"{self.nombre} está trayendo la pelota"


# Clase derivada: Gato
class Gato(Animal):
    """Clase que representa un gato"""

    def __init__(self, nombre: str, edad: int, color: str) -> None:
        """Constructor que llama al constructor de la clase padre"""
        super().__init__(nombre, edad, "Gato")
        self.color = color

    def describir(self):
        """Sobrescribe el método describir de la clase padre"""
        return f"{super().describir()} - Color: {self.color}"

    def hacer_sonido(self):
        """Sobrescribe el método hacer_sonido de la clase padre"""
        return f"{self.nombre} maúlla: ¡Miau!"

    def moverse(self):
        """Sobrescribe el método moverse de la clase padre"""
        return f"{self.nombre} está saltando elegantemente"

    def rasgunar(self):
        """Método específico de la clase Gato"""
        return f"{self.nombre} está rasguñando el sofá"


# Clase derivada: Pajaro
class Pajaro(Animal):
    """Clase que representa un pájaro"""

    def __init__(self, nombre, edad, tipo_pajaro):
        """Constructor que llama al constructor de la clase padre"""
        super().__init__(nombre, edad, "Pájaro")
        self.tipo_pajaro = tipo_pajaro

    def describir(self):
        """Sobrescribe el método describir de la clase padre"""
        return f"{super().describir()} - Tipo: {self.tipo_pajaro}"

    def hacer_sonido(self):
        """Sobrescribe el método hacer_sonido de la clase padre"""
        return f"{self.nombre} canta: ¡Pío pío!"

    def moverse(self):
        """Sobrescribe el método moverse de la clase padre"""
        return f"{self.nombre} está volando en el cielo"

    def hacer_nido(self):
        """Método específico de la clase Pajaro"""
        return f"{self.nombre} está construyendo un nido"


# Clase derivada: Pez
class Pez(Animal):
    """Clase que representa un pez"""

    def __init__(self, nombre, edad, tipo_pez):
        """Constructor que llama al constructor de la clase padre"""
        super().__init__(nombre, edad, "Pez")
        self.tipo_pez = tipo_pez

    def describir(self):
        """Sobrescribe el método describir de la clase padre"""
        return f"{super().describir()} - Tipo: {self.tipo_pez}"

    def hacer_sonido(self):
        """Sobrescribe el método hacer_sonido de la clase padre"""
        return f"{self.nombre} hace burbujas (sin sonido audible)"

    def moverse(self):
        """Sobrescribe el método moverse de la clase padre"""
        return f"{self.nombre} está nadando en el agua"


# Clase derivada: León
class Leon(Animal):
    """Clase que representa un león"""

    def __init__(self, nombre, edad, melena):
        """Constructor que llama al constructor de la clase padre"""
        super().__init__(nombre, edad, "León")
        self.melena = melena

    def describir(self):
        """Sobrescribe el método describir de la clase padre"""
        melena_desc = "con melena" if self.melena else "sin melena"
        return f"{super().describir()} - {melena_desc}"

    def hacer_sonido(self):
        """Sobrescribe el método hacer_sonido de la clase padre"""
        return f"{self.nombre} ruge: ¡ROOOOAAARRR!"

    def moverse(self):
        """Sobrescribe el método moverse de la clase padre"""
        return f"{self.nombre} está caminando majestuosamente"

    def cazar(self):
        """Método específico de la clase León"""
        return f"{self.nombre} está cazando presas"


# PROGRAMA PRINCIPAL
print("=" * 70)
print("EJEMPLO DE CLASES: ANIMALES Y SUS TIPOS")
print("=" * 70)

# Crear diferentes tipos de animales
perro = Perro("Max", 5, "Labrador")
gato = Gato("Whiskers", 3, "Naranja")
pajaro = Pajaro("Tweety", 2, "Canario")
pez = Pez("Nemo", 1, "Pez Payaso")
leon = Leon("Simba", 8, True)

# Lista de animales
animales = [perro, gato, pajaro, pez, leon]

# Mostrar información de cada animal
print("\nInformación de los animales:")
print("-" * 70)
for animal in animales:
    print(f"✓ {animal.describir()}")

# Demostrar polimorfismo (mismo método, diferentes comportamientos)
print("\nSonidos que hacen los animales (Polimorfismo):")
print("-" * 70)
for animal in animales:
    print(f"→ {animal.hacer_sonido()}")

print("\nCómo se mueven los animales:")
print("-" * 70)
for animal in animales:
    print(f"→ {animal.moverse()}")

# Demostrar métodos específicos de cada clase
print("\nAcciones específicas de cada animal:")
print("-" * 70)
print(f"🐕 {perro.traer_objeto()}")
print(f"🐱 {gato.rasgunar()}")
print(f"🐦 {pajaro.hacer_nido()}")
print(f"🦁 {leon.cazar()}")

# Crear más animales
print("\n" + "=" * 70)
print("Creando más animales:")
print("=" * 70)

perro2 = Perro("Buddy", 2, "Golden Retriever")
gato2 = Gato("Felix", 4, "Negro")
leon2 = Leon("Mufasa", 12, True)

animales_adicionales = [perro2, gato2, leon2]

for animal in animales_adicionales:
    print(f"\n✓ {animal.describir()}")
    print(f"  {animal.hacer_sonido()}")
    print(f"  {animal.moverse()}")
