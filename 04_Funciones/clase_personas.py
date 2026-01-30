# Ejemplo de Clases: Personas
# Este programa demuestra la herencia y polimorfismo con diferentes tipos de personas

# Clase padre: Persona
class Persona:
    """Clase base para todas las personas"""

    def __init__(self, nombre, edad, cedula):
        """Constructor para inicializar los atributos básicos"""
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula

    def describir(self):
        """Método para describir la persona"""
        return f"{self.nombre} ({self.edad} años) - Cédula: {self.cedula}"

    def saludar(self):
        """Método para saludar"""
        return f"Hola, mi nombre es {self.nombre}"

    def trabajar(self):
        """Método virtual que será sobrescrito en las clases derivadas"""
        return f"{self.nombre} está trabajando"


# Clase derivada: Estudiante
class Estudiante(Persona):
    """Clase que representa un estudiante"""

    def __init__(self, nombre, edad, cedula, matricula, grado):
        """Constructor que llama al constructor de la clase padre"""
        super().__init__(nombre, edad, cedula)
        self.matricula = matricula
        self.grado = grado
        self.calificaciones = []

    def describir(self):
        """Sobrescribe el método describir de la clase padre"""
        return f"{super().describir()} - Matrícula: {self.matricula} - Grado: {self.grado}"

    def trabajar(self):
        """Sobrescribe el método trabajar de la clase padre"""
        return f"{self.nombre} está estudiando en grado {self.grado}"

    def estudiar(self, materia):
        """Método específico de la clase Estudiante"""
        return f"{self.nombre} está estudiando {materia}"

    def agregar_calificacion(self, calificacion):
        """Agregar una calificación"""
        self.calificaciones.append(calificacion)
        return f"Calificación de {calificacion} agregada para {self.nombre}"

    def obtener_promedio(self):
        """Obtener el promedio de calificaciones"""
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)


# Clase derivada: Profesor
class Profesor(Persona):
    """Clase que representa un profesor"""

    def __init__(self, nombre, edad, cedula, especialidad, años_experiencia):
        """Constructor que llama al constructor de la clase padre"""
        super().__init__(nombre, edad, cedula)
        self.especialidad = especialidad
        self.años_experiencia = años_experiencia
        self.estudiantes = []

    def describir(self):
        """Sobrescribe el método describir de la clase padre"""
        return f"{super().describir()} - Especialidad: {self.especialidad} - Experiencia: {self.años_experiencia} años"

    def trabajar(self):
        """Sobrescribe el método trabajar de la clase padre"""
        return f"{self.nombre} está enseñando {self.especialidad}"

    def enseñar(self, materia):
        """Método específico de la clase Profesor"""
        return f"{self.nombre} está enseñando {materia} con {self.años_experiencia} años de experiencia"

    def calificar_estudiante(self, nombre_estudiante):
        """Método para calificar a un estudiante"""
        return f"{self.nombre} está calificando a {nombre_estudiante}"

    def agregar_estudiante(self, estudiante):
        """Agregar un estudiante a la clase"""
        self.estudiantes.append(estudiante)
        return f"{estudiante.nombre} ha sido agregado a la clase de {self.nombre}"


# Clase derivada: Ingeniero
class Ingeniero(Persona):
    """Clase que representa un ingeniero"""

    def __init__(self, nombre, edad, cedula, especialidad, empresa):
        """Constructor que llama al constructor de la clase padre"""
        super().__init__(nombre, edad, cedula)
        self.especialidad = especialidad
        self.empresa = empresa
        self.proyectos = []

    def describir(self):
        """Sobrescribe el método describir de la clase padre"""
        return f"{super().describir()} - Especialidad: {self.especialidad} - Empresa: {self.empresa}"

    def trabajar(self):
        """Sobrescribe el método trabajar de la clase padre"""
        return f"{self.nombre} está trabajando en {self.empresa} como ingeniero {self.especialidad}"

    def desarrollar_proyecto(self, nombre_proyecto):
        """Método específico de la clase Ingeniero"""
        self.proyectos.append(nombre_proyecto)
        return f"{self.nombre} está desarrollando el proyecto: {nombre_proyecto}"

    def completar_proyecto(self, nombre_proyecto):
        """Método para completar un proyecto"""
        if nombre_proyecto in self.proyectos:
            self.proyectos.remove(nombre_proyecto)
            return f"Proyecto '{nombre_proyecto}' completado por {self.nombre}"
        return f"Proyecto no encontrado en la lista de {self.nombre}"


# Clase derivada: Médico
class Medico(Persona):
    """Clase que representa un médico"""

    def __init__(self, nombre, edad, cedula, especialidad, licencia):
        """Constructor que llama al constructor de la clase padre"""
        super().__init__(nombre, edad, cedula)
        self.especialidad = especialidad
        self.licencia = licencia
        self.pacientes = []

    def describir(self):
        """Sobrescribe el método describir de la clase padre"""
        return f"{super().describir()} - Especialidad: {self.especialidad} - Licencia: {self.licencia}"

    def trabajar(self):
        """Sobrescribe el método trabajar de la clase padre"""
        return f"{self.nombre} está atendiendo pacientes como {self.especialidad}"

    def atender_paciente(self, nombre_paciente):
        """Método específico de la clase Médico"""
        return f"Dr. {self.nombre} está atendiendo a {nombre_paciente}"

    def diagnosticar(self, sintomas):
        """Método para hacer un diagnóstico"""
        return f"Dr. {self.nombre} diagnostica basado en: {sintomas}"

    def agregar_paciente(self, nombre_paciente):
        """Agregar un paciente"""
        self.pacientes.append(nombre_paciente)
        return f"{nombre_paciente} ha sido agregado como paciente de {self.nombre}"


# Clase derivada: Deportista
class Deportista(Persona):
    """Clase que representa un deportista"""

    def __init__(self, nombre, edad, cedula, deporte, equipo):
        """Constructor que llama al constructor de la clase padre"""
        super().__init__(nombre, edad, cedula)
        self.deporte = deporte
        self.equipo = equipo
        self.medallas = 0

    def describir(self):
        """Sobrescribe el método describir de la clase padre"""
        return f"{super().describir()} - Deporte: {self.deporte} - Equipo: {self.equipo}"

    def trabajar(self):
        """Sobrescribe el método trabajar de la clase padre"""
        return f"{self.nombre} está entrenando {self.deporte} para el equipo {self.equipo}"

    def entrenar(self):
        """Método específico de la clase Deportista"""
        return f"{self.nombre} está entrenando intensamente"

    def competir(self):
        """Método para competir"""
        return f"{self.nombre} está compitiendo en {self.deporte}"

    def ganar_medalla(self):
        """Ganar una medalla"""
        self.medallas += 1
        return f"{self.nombre} ha ganado una medalla! Total: {self.medallas}"


# PROGRAMA PRINCIPAL
print("=" * 80)
print("EJEMPLO DE CLASES: PERSONAS Y SUS TIPOS")
print("=" * 80)

# Crear diferentes tipos de personas
estudiante = Estudiante("Juan García", 16, "12345678", "EST001", "10")
profesor = Profesor("María López", 45, "87654321", "Matemáticas", 15)
ingeniero = Ingeniero("Carlos Rodríguez", 35,
                      "11223344", "Software", "TechCorp")
medico = Medico("Dr. Ana Silva", 50, "55667788", "Cardiología", "LIC-2020-001")
deportista = Deportista("Miguel Torres", 22, "99887766",
                        "Fútbol", "Real Madrid")

# Lista de personas
personas = [estudiante, profesor, ingeniero, medico, deportista]

# Mostrar información de cada persona
print("\nInformación de las personas:")
print("-" * 80)
for persona in personas:
    print(f"✓ {persona.describir()}")

# Demostrar polimorfismo (mismo método, diferentes comportamientos)
print("\nActividades principales (Polimorfismo):")
print("-" * 80)
for persona in personas:
    print(f"→ {persona.trabajar()}")

print("\nSaludos:")
print("-" * 80)
for persona in personas:
    print(f"→ {persona.saludar()}")

# Demostrar métodos específicos de cada clase
print("\nAcciones específicas de cada tipo de persona:")
print("-" * 80)
print(f"📚 {estudiante.estudiar('Química')}")
print(f"   {estudiante.agregar_calificacion(9.5)}")
print(f"   {estudiante.agregar_calificacion(8.7)}")
print(
    f"   Promedio de {estudiante.nombre}: {estudiante.obtener_promedio():.1f}")

print(f"\n👨‍🏫 {profesor.enseñar('Álgebra')}")
print(f"   {profesor.agregar_estudiante(estudiante)}")

print(f"\n💻 {ingeniero.desarrollar_proyecto('Sistema de Gestión')}")
print(f"   Proyectos activos: {', '.join(ingeniero.proyectos)}")

print(f"\n⚕️ {medico.atender_paciente('Pedro Martínez')}")
print(f"   {medico.diagnosticar('Fiebre y tos')}")

print(f"\n⚽ {deportista.entrenar()}")
print(f"   {deportista.competir()}")
print(f"   {deportista.ganar_medalla()}")

# Crear más personas
print("\n" + "=" * 80)
print("Creando más personas:")
print("=" * 80)

estudiante2 = Estudiante("Ana Martínez", 15, "44556677", "EST002", "9")
profesor2 = Profesor("Roberto Díaz", 38, "22334455", "Física", 10)

personas_adicionales = [estudiante2, profesor2]

for persona in personas_adicionales:
    print(f"\n✓ {persona.describir()}")
    print(f"  {persona.trabajar()}")

print("\n" + "=" * 80)
