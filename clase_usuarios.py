# Ejemplo de Clases: Usuarios, Empleados, Vendedores y más
# Este programa demuestra la herencia y polimorfismo en un sistema de usuarios

# Clase padre: Usuario
class Usuario:
    """Clase base para todos los usuarios del sistema"""

    def __init__(self, usuario_id, nombre, email, telefono, password):
        """Constructor para inicializar los atributos básicos"""
        self.usuario_id = usuario_id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.password = password
        self.activo = True
        self.fecha_registro = "2024-01-13"

    def describir(self):
        """Método para describir el usuario"""
        estado = "Activo" if self.activo else "Inactivo"
        return f"ID: {self.usuario_id} - {self.nombre} ({self.email}) - {estado}"

    def saludar(self):
        """Método para saludar"""
        return f"Hola, soy {self.nombre}"

    def cambiar_email(self, nuevo_email):
        """Cambiar el email del usuario"""
        self.email = nuevo_email
        return f"Email actualizado a {nuevo_email}"

    def cambiar_password(self, password_actual, password_nuevo):
        """Cambiar la contraseña del usuario"""
        if self.password == password_actual:
            self.password = password_nuevo
            return f"Contraseña de {self.nombre} actualizada exitosamente"
        return f"Contraseña actual incorrecta"

    def validar_password(self, password):
        """Validar la contraseña ingresada"""
        return self.password == password

    def actualizar_perfil(self):
        """Método virtual que será sobrescrito en las clases derivadas"""
        return f"Perfil de {self.nombre} actualizado"


# Clase derivada: Cliente
class Cliente(Usuario):
    """Clase que representa un cliente"""

    def __init__(self, usuario_id, nombre, email, telefono, password, direccion):
        """Constructor que llama al constructor de la clase padre"""
        super().__init__(usuario_id, nombre, email, telefono, password)
        self.direccion = direccion
        self.compras = []
        self.saldo = 0

    def describir(self):
        """Sobrescribe el método describir de la clase padre"""
        return f"Cliente: {super().describir()} - Dirección: {self.direccion}"

    def actualizar_perfil(self):
        """Sobrescribe el método actualizar_perfil de la clase padre"""
        return f"Perfil de cliente {self.nombre} actualizado con dirección: {self.direccion}"

    def hacer_compra(self, producto, cantidad, precio):
        """Método específico de la clase Cliente"""
        compra = {
            "producto": producto,
            "cantidad": cantidad,
            "precio": precio,
            "total": cantidad * precio
        }
        self.compras.append(compra)
        return f"{self.nombre} compró {cantidad} de {producto} por ${compra['total']}"

    def obtener_historial_compras(self):
        """Obtener historial de compras"""
        if not self.compras:
            return f"{self.nombre} no ha realizado compras"
        total = sum(c["total"] for c in self.compras)
        return f"{self.nombre} ha realizado {len(self.compras)} compras por un total de ${total}"

    def agregar_saldo(self, cantidad):
        """Agregar saldo a la cuenta"""
        self.saldo += cantidad
        return f"Saldo agregado: ${cantidad}. Nuevo saldo: ${self.saldo}"


# Clase derivada: Empleado
class Empleado(Usuario):
    """Clase que representa un empleado"""

    def __init__(self, usuario_id, nombre, email, telefono, password, numero_empleado, departamento, salario):
        """Constructor que llama al constructor de la clase padre"""
        super().__init__(usuario_id, nombre, email, telefono, password)
        self.numero_empleado = numero_empleado
        self.departamento = departamento
        self.salario = salario
        self.tareas = []

    def describir(self):
        """Sobrescribe el método describir de la clase padre"""
        return f"Empleado: {super().describir()} - Depto: {self.departamento} - Salario: ${self.salario}"

    def actualizar_perfil(self):
        """Sobrescribe el método actualizar_perfil de la clase padre"""
        return f"Perfil de empleado {self.nombre} en {self.departamento} actualizado"

    def asignar_tarea(self, tarea):
        """Asignar una tarea al empleado"""
        self.tareas.append({"tarea": tarea, "completada": False})
        return f"Tarea '{tarea}' asignada a {self.nombre}"

    def completar_tarea(self, indice):
        """Marcar una tarea como completada"""
        if 0 <= indice < len(self.tareas):
            self.tareas[indice]["completada"] = True
            return f"Tarea '{self.tareas[indice]['tarea']}' completada por {self.nombre}"
        return "Tarea no encontrada"

    def obtener_tareas_pendientes(self):
        """Obtener tareas pendientes"""
        pendientes = [t for t in self.tareas if not t["completada"]]
        return f"{self.nombre} tiene {len(pendientes)} tareas pendientes"


# Clase derivada: Vendedor
class Vendedor(Empleado):
    """Clase que representa un vendedor"""

    def __init__(self, usuario_id, nombre, email, telefono, password, numero_empleado, departamento, salario, zona):
        """Constructor que llama al constructor de la clase padre"""
        super().__init__(usuario_id, nombre, email, telefono, password,
                         numero_empleado, departamento, salario)
        self.zona = zona
        self.ventas = []
        self.comisiones = 0

    def describir(self):
        """Sobrescribe el método describir de la clase padre"""
        return f"Vendedor: {super().describir()} - Zona: {self.zona}"

    def actualizar_perfil(self):
        """Sobrescribe el método actualizar_perfil de la clase padre"""
        return f"Perfil del vendedor {self.nombre} en zona {self.zona} actualizado"

    def registrar_venta(self, cliente, producto, cantidad, precio):
        """Registrar una venta"""
        venta = {
            "cliente": cliente,
            "producto": producto,
            "cantidad": cantidad,
            "precio": precio,
            "total": cantidad * precio
        }
        self.ventas.append(venta)
        comision = venta["total"] * 0.05  # 5% de comisión
        self.comisiones += comision
        return f"{self.nombre} vendió {cantidad} de {producto} a {cliente} - Comisión: ${comision:.2f}"

    def obtener_total_ventas(self):
        """Obtener el total de ventas"""
        total = sum(v["total"] for v in self.ventas)
        return f"{self.nombre} ha vendido un total de ${total} con comisiones de ${self.comisiones:.2f}"


# Clase derivada: Gerente
class Gerente(Empleado):
    """Clase que representa un gerente"""

    def __init__(self, usuario_id, nombre, email, telefono, password, numero_empleado, departamento, salario, equipo_size):
        """Constructor que llama al constructor de la clase padre"""
        super().__init__(usuario_id, nombre, email, telefono, password,
                         numero_empleado, departamento, salario)
        self.equipo_size = equipo_size
        self.equipo = []
        self.presupuesto = 0

    def describir(self):
        """Sobrescribe el método describir de la clase padre"""
        return f"Gerente: {super().describir()} - Equipo: {len(self.equipo)}/{self.equipo_size}"

    def actualizar_perfil(self):
        """Sobrescribe el método actualizar_perfil de la clase padre"""
        return f"Perfil del gerente {self.nombre} del departamento {self.departamento} actualizado"

    def agregar_empleado_a_equipo(self, empleado):
        """Agregar un empleado al equipo"""
        if len(self.equipo) < self.equipo_size:
            self.equipo.append(empleado)
            return f"Empleado {empleado.nombre} agregado al equipo de {self.nombre}"
        return f"El equipo de {self.nombre} está lleno"

    def asignar_presupuesto(self, cantidad):
        """Asignar un presupuesto"""
        self.presupuesto = cantidad
        return f"Presupuesto de ${cantidad} asignado a {self.nombre}"

    def obtener_informe_equipo(self):
        """Obtener informe del equipo"""
        if not self.equipo:
            return f"{self.nombre} no tiene empleados en su equipo"
        nombres_equipo = ", ".join([e.nombre for e in self.equipo])
        return f"{self.nombre} supervisa a: {nombres_equipo}"


# Clase derivada: Administrador
class Administrador(Usuario):
    """Clase que representa un administrador del sistema"""

    def __init__(self, usuario_id, nombre, email, telefono, password, nivel_acceso):
        """Constructor que llama al constructor de la clase padre"""
        super().__init__(usuario_id, nombre, email, telefono, password)
        self.nivel_acceso = nivel_acceso
        self.logs = []

    def describir(self):
        """Sobrescribe el método describir de la clase padre"""
        return f"Administrador: {super().describir()} - Nivel: {self.nivel_acceso}"

    def actualizar_perfil(self):
        """Sobrescribe el método actualizar_perfil de la clase padre"""
        return f"Perfil del administrador {self.nombre} actualizado"

    def registrar_log(self, accion):
        """Registrar una acción en el log"""
        self.logs.append({"accion": accion, "timestamp": "2024-01-13 10:30"})
        return f"Acción registrada: {accion}"

    def desactivar_usuario(self, usuario):
        """Desactivar un usuario"""
        usuario.activo = False
        self.registrar_log(f"Usuario {usuario.nombre} desactivado")
        return f"Usuario {usuario.nombre} ha sido desactivado por {self.nombre}"

    def obtener_logs(self):
        """Obtener los logs del administrador"""
        return f"{self.nombre} tiene {len(self.logs)} acciones registradas"


# Clase derivada: Soporte Técnico
class SoporteTecnico(Empleado):
    """Clase que representa un técnico de soporte"""

    def __init__(self, usuario_id, nombre, email, telefono, numero_empleado, departamento, salario, especializacion):
        """Constructor que llama al constructor de la clase padre"""
        super().__init__(usuario_id, nombre, email, telefono,
                         numero_empleado, departamento, salario)
        self.especializacion = especializacion
        self.tickets = []

    def describir(self):
        """Sobrescribe el método describir de la clase padre"""
        return f"Soporte Técnico: {super().describir()} - Especialización: {self.especializacion}"

    def actualizar_perfil(self):
        """Sobrescribe el método actualizar_perfil de la clase padre"""
        return f"Perfil del técnico {self.nombre} especializado en {self.especializacion} actualizado"

    def crear_ticket(self, cliente, problema):
        """Crear un ticket de soporte"""
        ticket = {
            "cliente": cliente,
            "problema": problema,
            "estado": "Abierto",
            "resuelto": False
        }
        self.tickets.append(ticket)
        return f"Ticket creado para {cliente}: {problema}"

    def resolver_ticket(self, indice):
        """Resolver un ticket"""
        if 0 <= indice < len(self.tickets):
            self.tickets[indice]["resuelto"] = True
            self.tickets[indice]["estado"] = "Resuelto"
            return f"Ticket de {self.tickets[indice]['cliente']} resuelto por {self.nombre}"
        return "Ticket no encontrado"

    def obtener_tickets_abiertos(self):
        """Obtener tickets abiertos"""
        abiertos = [t for t in self.tickets if not t["resuelto"]]
        return f"{self.nombre} tiene {len(abiertos)} tickets abiertos"


# PROGRAMA PRINCIPAL
print("=" * 90)
print("EJEMPLO DE CLASES: USUARIOS, EMPLEADOS, VENDEDORES Y MÁS")
print("=" * 90)

# Crear diferentes tipos de usuarios
cliente1 = Cliente("CLI001", "Juan Pérez", "juan@email.com",
                   "555-1234", "pass123", "Calle 123")
cliente2 = Cliente("CLI002", "María García",
                   "maria@email.com", "555-5678", "pass456", "Avenida 456")
vendedor1 = Vendedor("EMP001", "Carlos López", "carlos@email.com",
                     "555-9999", "vendpass1", "V001", "Ventas", 2000, "Norte")
gerente1 = Gerente("EMP002", "Patricia Rodríguez",
                   "patricia@email.com", "555-8888", "gerentpass1", "G001", "Ventas", 3500, 5)
soporte1 = SoporteTecnico("EMP003", "Roberto Díaz", "roberto@email.com",
                          "555-7777", "soportepass1", "S001", "Soporte", 2200, "Software")
admin1 = Administrador("ADM001", "Laura Silva",
                       "laura@email.com", "555-6666", "adminpass1", "Super")

# Lista de usuarios
usuarios = [cliente1, cliente2, vendedor1, gerente1, soporte1, admin1]

# Mostrar información de cada usuario
print("\nInformación de todos los usuarios:")
print("-" * 90)
for usuario in usuarios:
    print(f"✓ {usuario.describir()}")

# Demostrar polimorfismo
print("\nActualizando perfiles (Polimorfismo):")
print("-" * 90)
for usuario in usuarios:
    print(f"→ {usuario.actualizar_perfil()}")

print("\nSaludos:")
print("-" * 90)
for usuario in usuarios:
    print(f"→ {usuario.saludar()}")

# Acciones específicas de cada tipo de usuario
print("\nAcciones específicas de cada tipo de usuario:")
print("=" * 90)

# Cliente
print("\n👤 CLIENTE:")
print("-" * 90)
print(f"{cliente1.hacer_compra('Laptop', 1, 800)}")
print(f"{cliente1.hacer_compra('Mouse', 2, 25)}")
print(f"{cliente1.obtener_historial_compras()}")
print(f"{cliente1.agregar_saldo(100)}")

# Vendedor
print("\n💼 VENDEDOR:")
print("-" * 90)
print(f"{vendedor1.registrar_venta(cliente1.nombre, 'Teclado', 3, 50)}")
print(f"{vendedor1.registrar_venta(cliente2.nombre, 'Monitor', 1, 300)}")
print(f"{vendedor1.obtener_total_ventas()}")
print(f"{vendedor1.asignar_tarea('Llamar a clientes nuevos')}")

# Gerente
print("\n👔 GERENTE:")
print("-" * 90)
print(f"{gerente1.agregar_empleado_a_equipo(vendedor1)}")
print(f"{gerente1.asignar_presupuesto(50000)}")
print(f"{gerente1.asignar_tarea('Revisar reporte mensual')}")
print(f"{gerente1.obtener_informe_equipo()}")
print(f"{gerente1.obtener_tareas_pendientes()}")

# Soporte Técnico
print("\n🔧 SOPORTE TÉCNICO:")
print("-" * 90)
print(f"{soporte1.crear_ticket(cliente1.nombre, 'Problema con instalación')}")
print(f"{soporte1.crear_ticket(cliente2.nombre, 'No enciende el dispositivo')}")
print(f"{soporte1.resolver_ticket(0)}")
print(f"{soporte1.obtener_tickets_abiertos()}")

# Administrador
print("\n🛡️ ADMINISTRADOR:")
print("-" * 90)
print(f"{admin1.registrar_log('Backup del sistema completado')}")
print(f"{admin1.registrar_log('Usuario nuevo creado')}")
print(f"{admin1.obtener_logs()}")
print(f"{admin1.desactivar_usuario(cliente1)}")

# Demostración de funciones de contraseña
print("\n" + "=" * 90)
print("GESTIÓN DE CONTRASEÑAS:")
print("-" * 90)
print(
    f"✓ Validar password de {cliente2.nombre}: {cliente2.validar_password('pass456')}")
print(
    f"✓ Validar password incorrecto: {cliente2.validar_password('wrongpass')}")
print(f"✓ {cliente2.cambiar_password('pass456', 'newpass789')}")
print(f"✓ Validar nuevo password: {cliente2.validar_password('newpass789')}")
print(f"✓ {vendedor1.cambiar_password('vendpass1', 'newvendpass')}")

# Crear más usuarios
print("\n" + "=" * 90)
print("Creando más usuarios:")
print("=" * 90)

cliente3 = Cliente("CLI003", "Ana Martínez",
                   "ana@email.com", "555-4444", "pass789", "Plaza 789")
vendedor2 = Vendedor("EMP004", "Diego Torres", "diego@email.com",
                     "555-3333", "diegopass1", "V002", "Ventas", 2000, "Sur")

usuarios_adicionales = [cliente3, vendedor2]

for usuario in usuarios_adicionales:
    print(f"\n✓ {usuario.describir()}")
    print(f"  {usuario.actualizar_perfil()}")

print("\n" + "=" * 90)
