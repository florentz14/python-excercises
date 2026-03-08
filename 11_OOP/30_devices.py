# -------------------------------------------------
# File Name: 30_devices.py
# Author: Florentino Báez
# Date: 11_OOP
# Description: Demonstrates inheritance and polymorphism with mobile devices.
# -------------------------------------------------

class DispositivoMovil:
    """Clase base para todos los dispositivos móviles"""

    def __init__(self, marca, modelo, año):
        """Constructor para inicializar los atributos básicos"""
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False

    def describir(self):
        """Método para describir el dispositivo"""
        return f"{self.marca} {self.modelo} ({self.año})"

    def encender(self):
        """Encender el dispositivo"""
        self.encendido = True
        return f"{self.marca} {self.modelo} se ha encendido"

    def apagar(self):
        """Apagar el dispositivo"""
        self.encendido = False
        return f"{self.marca} {self.modelo} se ha apagado"

    def hacer_llamada(self, numero):
        """Método virtual que será sobrescrito en las clases derivadas"""
        if self.encendido:
            return f"Realizando llamada a {numero}"
        return f"El dispositivo está apagado"


# Clase derivada: Smartphone
class Smartphone(DispositivoMovil):
    """Clase que representa un smartphone"""

    def __init__(self, marca, modelo, año, sistema_operativo, pantalla_inches):
        """Constructor que llama al constructor de la clase padre"""
        super().__init__(marca, modelo, año)
        self.sistema_operativo = sistema_operativo
        self.pantalla_inches = pantalla_inches
        self.aplicaciones = []

    def describir(self):
        """Sobrescribe el método describir de la clase padre"""
        return f"Smartphone: {super().describir()} - {self.sistema_operativo} - {self.pantalla_inches}\" - Apps: {len(self.aplicaciones)}"

    def hacer_llamada(self, numero):
        """Sobrescribe el método hacer_llamada de la clase padre"""
        if self.encendido:
            return f"Llamada del Smartphone {self.marca} a {numero}"
        return f"El Smartphone está apagado"

    def instalar_aplicacion(self, app_nombre):
        """Método específico de la clase Smartphone"""
        self.aplicaciones.append(app_nombre)
        return f"Aplicación '{app_nombre}' instalada en {self.marca}"

    def enviar_sms(self, numero, mensaje):
        """Método para enviar SMS"""
        if self.encendido:
            return f"SMS enviado a {numero}: '{mensaje}'"
        return "El Smartphone está apagado"

    def abrir_aplicacion(self, app_nombre):
        """Método para abrir una aplicación"""
        if app_nombre in self.aplicaciones:
            return f"Abriendo {app_nombre} en {self.marca}"
        return f"Aplicación '{app_nombre}' no está instalada"


# Clase derivada: Tablet
class Tablet(DispositivoMovil):
    """Clase que representa una tablet"""

    def __init__(self, marca, modelo, año, sistema_operativo, pantalla_inches):
        """Constructor que llama al constructor de la clase padre"""
        super().__init__(marca, modelo, año)
        self.sistema_operativo = sistema_operativo
        self.pantalla_inches = pantalla_inches

    def describir(self):
        """Sobrescribe el método describir de la clase padre"""
        return f"Tablet: {super().describir()} - {self.sistema_operativo} - {self.pantalla_inches}\""

    def hacer_llamada(self, numero):
        """Sobrescribe el método hacer_llamada de la clase padre"""
        return f"Las tablets no pueden hacer llamadas telefónicas"

    def ver_video(self):
        """Método específico de la clase Tablet"""
        if self.encendido:
            return f"Viendo video en {self.marca} con pantalla de {self.pantalla_inches}\""
        return "La Tablet está apagada"

    def dibujar(self):
        """Método para dibujar"""
        if self.encendido:
            return f"Dibujando en la Tablet {self.marca}"
        return "La Tablet está apagada"


# Clase derivada: Teléfono Básico
class TelefonoBasico(DispositivoMovil):
    """Clase que representa un teléfono básico (sin acceso a internet)"""

    def __init__(self, marca, modelo, año, bateria_horas):
        """Constructor que llama al constructor de la clase padre"""
        super().__init__(marca, modelo, año)
        self.bateria_horas = bateria_horas

    def describir(self):
        """Sobrescribe el método describir de la clase padre"""
        return f"Teléfono Básico: {super().describir()} - Batería: {self.bateria_horas}h"

    def hacer_llamada(self, numero):
        """Sobrescribe el método hacer_llamada de la clase padre"""
        if self.encendido:
            return f"Llamada desde {self.marca} al número {numero}"
        return "El teléfono está apagado"

    def enviar_sms(self, numero, mensaje):
        """Método para enviar SMS"""
        if self.encendido:
            return f"SMS enviado a {numero}: '{mensaje}'"
        return "El teléfono está apagado"

    def verificar_bateria(self):
        """Método para verificar batería"""
        return f"Batería disponible: {self.bateria_horas} horas"


# Clase derivada: Smartwatch
class Smartwatch(DispositivoMovil):
    """Clase que representa un smartwatch (reloj inteligente)"""

    def __init__(self, marca, modelo, año, pantalla_tamaño):
        """Constructor que llama al constructor de la clase padre"""
        super().__init__(marca, modelo, año)
        self.pantalla_tamaño = pantalla_tamaño
        self.sensores = []

    def describir(self):
        """Sobrescribe el método describir de la clase padre"""
        return f"Smartwatch: {super().describir()} - Pantalla: {self.pantalla_tamaño}\" - Sensores: {len(self.sensores)}"

    def hacer_llamada(self, numero):
        """Sobrescribe el método hacer_llamada de la clase padre"""
        if self.encendido:
            return f"Mini-llamada del Smartwatch {self.marca} a {numero}"
        return "El Smartwatch está apagado"

    def agregar_sensor(self, tipo_sensor):
        """Método específico de la clase Smartwatch"""
        self.sensores.append(tipo_sensor)
        return f"Sensor '{tipo_sensor}' agregado al {self.marca}"

    def medir_pasos(self):
        """Método para medir pasos"""
        if self.encendido:
            return f"Contando pasos con el Smartwatch {self.marca}"
        return "El Smartwatch está apagado"

    def medir_frecuencia_cardiaca(self):
        """Método para medir frecuencia cardíaca"""
        if self.encendido:
            return f"Midiendo frecuencia cardíaca con el Smartwatch {self.marca}"
        return "El Smartwatch está apagado"


# Clase derivada: E-reader
class EReader(DispositivoMovil):
    """Clase que representa un lector electrónico de libros"""

    def __init__(self, marca, modelo, año, pantalla_tamaño):
        """Constructor que llama al constructor de la clase padre"""
        super().__init__(marca, modelo, año)
        self.pantalla_tamaño = pantalla_tamaño
        self.libros = []

    def describir(self):
        """Sobrescribe el método describir de la clase padre"""
        return f"E-Reader: {super().describir()} - Pantalla: {self.pantalla_tamaño}\" - Libros: {len(self.libros)}"

    def hacer_llamada(self, numero):
        """Sobrescribe el método hacer_llamada de la clase padre"""
        return f"Los E-readers no pueden hacer llamadas"

    def descargar_libro(self, titulo):
        """Método específico de la clase EReader"""
        self.libros.append(titulo)
        return f"Libro '{titulo}' descargado en {self.marca}"

    def leer_libro(self, titulo):
        """Método para leer un libro"""
        if titulo in self.libros and self.encendido:
            return f"Leyendo '{titulo}' en el {self.marca}"
        elif not self.encendido:
            return "El E-reader está apagado"
        else:
            return f"El libro '{titulo}' no está disponible"


# PROGRAMA PRINCIPAL
print("=" * 90)
print("EJEMPLO DE CLASES: DISPOSITIVOS MÓVILES Y SUS TIPOS")
print("=" * 90)

# Crear diferentes tipos de dispositivos móviles
smartphone = Smartphone("Apple", "iPhone 15", 2023, "iOS 17", 6.1)
tablet = Tablet("Samsung", "Galaxy Tab S9", 2023, "Android 13", 11)
telefono_basico = TelefonoBasico("Nokia", "3310", 2000, 240)
smartwatch = Smartwatch("Apple", "Watch Series 9", 2023, 1.9)
ereader = EReader("Amazon", "Kindle Paperwhite", 2023, 6.8)

# Lista de dispositivos
dispositivos = [smartphone, tablet, telefono_basico, smartwatch, ereader]

# Mostrar información de cada dispositivo
print("\nInformación de los dispositivos móviles:")
print("-" * 90)
for dispositivo in dispositivos:
    print(f"✓ {dispositivo.describir()}")

# Encender todos los dispositivos
print("\nEncendiendo dispositivos:")
print("-" * 90)
for dispositivo in dispositivos:
    print(f"→ {dispositivo.encender()}")

# Demostrar polimorfismo (mismo método, diferentes comportamientos)
print("\nHaciendo llamadas (Polimorfismo):")
print("-" * 90)
for dispositivo in dispositivos:
    print(f"→ {dispositivo.hacer_llamada('555-1234')}")

# Demostrar métodos específicos de cada clase
print("\nAcciones específicas de cada dispositivo:")
print("-" * 90)
print(f"📱 {smartphone.instalar_aplicacion('WhatsApp')}")
print(f"   {smartphone.instalar_aplicacion('Instagram')}")
print(f"   {smartphone.abrir_aplicacion('WhatsApp')}")
print(f"   {smartphone.enviar_sms('555-5678', 'Hola cómo estás?')}")

print(f"\n📊 {tablet.ver_video()}")
print(f"   {tablet.dibujar()}")

print(f"\n☎️ {telefono_basico.enviar_sms('555-9999', 'Hola!')}")
print(f"   {telefono_basico.verificar_bateria()}")

print(f"\n⌚ {smartwatch.agregar_sensor('Acelerómetro')}")
print(f"   {smartwatch.agregar_sensor('Sensor cardíaco')}")
print(f"   {smartwatch.medir_pasos()}")
print(f"   {smartwatch.medir_frecuencia_cardiaca()}")

print(f"\n📖 {ereader.descargar_libro('Don Quijote')}")
print(f"   {ereader.descargar_libro('Cien años de soledad')}")
print(f"   {ereader.leer_libro('Don Quijote')}")

# Apagar todos los dispositivos
print("\n" + "=" * 90)
print("Apagando dispositivos:")
print("-" * 90)
for dispositivo in dispositivos:
    print(f"→ {dispositivo.apagar()}")

# Crear más dispositivos
print("\n" + "=" * 90)
print("Creando más dispositivos:")
print("=" * 90)

smartphone2 = Smartphone("Samsung", "Galaxy S24", 2024, "Android 14", 6.2)
tablet2 = Tablet("Apple", "iPad Pro", 2023, "iPadOS 17", 12.9)

dispositivos_adicionales = [smartphone2, tablet2]

for dispositivo in dispositivos_adicionales:
    print(f"\n✓ {dispositivo.describir()}")
    print(f"  {dispositivo.encender()}")
    dispositivo.encendido = True
    if isinstance(dispositivo, Smartphone):
        print(f"  {dispositivo.instalar_aplicacion('Spotify')}")

print("\n" + "=" * 90)
