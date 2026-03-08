# -------------------------------------------------
# File Name: 38_advanced_users.py
# Author: Florentino Báez
# Date: 11_OOP
# Description: Advanced user management with secure password hashing,
# -------------------------------------------------

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Dict, Optional, Set, Tuple
import hashlib
import hmac
import secrets
import uuid


UTC = timezone.utc


def now_utc() -> datetime:
    """Obtener la hora actual en UTC"""
    return datetime.now(UTC)


# -------------------------
# Hasheo seguro de contraseñas (PBKDF2)
# -------------------------

class PasswordHasher:
    """
    Hasheo seguro de contraseñas usando PBKDF2-HMAC-SHA256.
    Almacena: algoritmo, iteraciones, salt, hash.
    """
    algorithm = "pbkdf2_sha256"

    def __init__(self, iterations: int = 200_000, salt_bytes: int = 16):
        """
        Inicializar el hasher de contraseñas

        Args:
            iterations: Número de iteraciones PBKDF2 (por defecto 200,000)
            salt_bytes: Bytes de salt aleatorio (por defecto 16)
        """
        self.iterations = iterations
        self.salt_bytes = salt_bytes

    def hash_password(self, plain_password: str) -> str:
        """
        Hashear una contraseña en texto plano

        Args:
            plain_password: Contraseña en texto plano

        Returns:
            String con formato: algorithm$iterations$salt$hash

        Raises:
            ValueError: Si la contraseña es muy corta
        """
        if not plain_password or len(plain_password) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres.")

        salt = secrets.token_bytes(self.salt_bytes)
        dk = hashlib.pbkdf2_hmac(
            "sha256",
            plain_password.encode("utf-8"),
            salt,
            self.iterations,
        )
        # Codificar en hexadecimal para portabilidad
        return f"{self.algorithm}${self.iterations}${salt.hex()}${dk.hex()}"

    def verify_password(self, plain_password: str, stored: str) -> bool:
        """
        Verificar una contraseña contra su hash almacenado

        Args:
            plain_password: Contraseña en texto plano
            stored: Hash almacenado

        Returns:
            True si la contraseña es correcta, False si no
        """
        try:
            algorithm, iters_str, salt_hex, hash_hex = stored.split("$", 3)
            if algorithm != self.algorithm:
                return False

            iters = int(iters_str)
            salt = bytes.fromhex(salt_hex)

            dk = hashlib.pbkdf2_hmac(
                "sha256",
                plain_password.encode("utf-8"),
                salt,
                iters,
            )
            # Comparación en tiempo constante para evitar timing attacks
            return hmac.compare_digest(dk.hex(), hash_hex)
        except Exception:
            return False


# -------------------------
# Modelo de Usuario Avanzado
# -------------------------

@dataclass
class UsuarioAvanzado:
    """Modelo avanzado de usuario con seguridad y auditoría"""

    # Identidad
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    username: str = ""
    email: str = ""

    # Autenticación
    password_hash: str = ""
    is_active: bool = True
    is_email_verified: bool = False
    mfa_enabled: bool = False  # Bandera para autenticación de dos factores

    # Autorización
    roles: Set[str] = field(default_factory=set)
    permissions: Set[str] = field(default_factory=set)

    # Seguridad y auditoría
    failed_login_attempts: int = 0  # Intentos fallidos de login
    locked_until: Optional[datetime] = None  # Hora hasta la que está bloqueado
    last_login_at: Optional[datetime] = None  # Último login
    last_login_ip: Optional[str] = None  # IP del último login

    # Timestamps de auditoría
    created_at: datetime = field(default_factory=now_utc)
    updated_at: datetime = field(default_factory=now_utc)

    # Perfil
    full_name: Optional[str] = None
    phone: Optional[str] = None
    timezone: str = "America/New_York"
    locale: str = "es-ES"

    # Soft delete (borrado lógico)
    deleted_at: Optional[datetime] = None

    def mark_updated(self) -> None:
        """Marcar el usuario como actualizado"""
        self.updated_at = now_utc()

    def is_locked(self) -> bool:
        """Verificar si el usuario está bloqueado"""
        return self.locked_until is not None and self.locked_until > now_utc()

    def can_login(self) -> bool:
        """Verificar si el usuario puede hacer login"""
        return self.is_active and self.deleted_at is None and not self.is_locked()

    def get_info(self) -> str:
        """Obtener información del usuario"""
        estado = "🟢 Activo" if self.is_active else "🔴 Inactivo"
        bloqueado = " (BLOQUEADO)" if self.is_locked() else ""
        verificado = "✓" if self.is_email_verified else "✗"
        return f"ID: {self.id[:8]}... | {self.username} | {self.email} | {estado}{bloqueado} | Verificado: {verificado}"


# -------------------------
# Gestor avanzado de usuarios
# -------------------------

class GestorUsuarios:
    """
    Gestión avanzada de usuarios en memoria.
    Fácilmente migrables a base de datos después.
    """

    def __init__(
        self,
        hasher: Optional[PasswordHasher] = None,
        max_failed_attempts: int = 5,
        lock_minutes: int = 15,
        session_minutes: int = 60,
    ):
        """
        Inicializar el gestor de usuarios

        Args:
            hasher: Instancia de PasswordHasher
            max_failed_attempts: Máximo de intentos fallidos antes de bloquear
            lock_minutes: Minutos para bloquear la cuenta
            session_minutes: Duración de sesión en minutos
        """
        self.hasher = hasher or PasswordHasher()
        self.max_failed_attempts = max_failed_attempts
        self.lock_duration = timedelta(minutes=lock_minutes)
        self.session_duration = timedelta(minutes=session_minutes)

        # Almacenamiento
        self._users_by_id: Dict[str, UsuarioAvanzado] = {}
        self._users_by_username: Dict[str, str] = {}
        self._users_by_email: Dict[str, str] = {}

        # Almacenamiento de sesiones: token -> (user_id, expires_at)
        self._sessions: Dict[str, Tuple[str, datetime]] = {}

    # ---------- Helpers de validación ----------

    @staticmethod
    def _normalize_username(username: str) -> str:
        """Normalizar nombre de usuario"""
        return username.strip().lower()

    @staticmethod
    def _normalize_email(email: str) -> str:
        """Normalizar email"""
        return email.strip().lower()

    @staticmethod
    def _validate_username(username: str) -> None:
        """Validar formato de nombre de usuario"""
        if len(username) < 3:
            raise ValueError(
                "El nombre de usuario debe tener al menos 3 caracteres.")
        if " " in username:
            raise ValueError(
                "El nombre de usuario no puede contener espacios.")

    @staticmethod
    def _validate_email(email: str) -> None:
        """Validar formato de email"""
        if "@" not in email or "." not in email.split("@")[-1]:
            raise ValueError("Formato de email inválido.")

    # ---------- Operaciones principales ----------

    def register_user(
        self,
        username: str,
        email: str,
        plain_password: str,
        full_name: Optional[str] = None,
        phone: Optional[str] = None,
        roles: Optional[Set[str]] = None,
    ) -> UsuarioAvanzado:
        """
        Registrar un nuevo usuario

        Args:
            username: Nombre de usuario único
            email: Email único
            plain_password: Contraseña en texto plano (será hasheada)
            full_name: Nombre completo
            phone: Número de teléfono
            roles: Conjunto de roles (por defecto {"user"})

        Returns:
            Objeto UsuarioAvanzado creado

        Raises:
            ValueError: Si username/email ya existen o son inválidos
        """
        username_n = self._normalize_username(username)
        email_n = self._normalize_email(email)

        self._validate_username(username_n)
        self._validate_email(email_n)

        if username_n in self._users_by_username:
            raise ValueError("El nombre de usuario ya existe.")
        if email_n in self._users_by_email:
            raise ValueError("El email ya está registrado.")

        password_hash = self.hasher.hash_password(plain_password)

        user = UsuarioAvanzado(
            username=username_n,
            email=email_n,
            password_hash=password_hash,
            full_name=full_name,
            phone=phone,
            roles=set(roles or {"user"}),
        )

        self._users_by_id[user.id] = user
        self._users_by_username[username_n] = user.id
        self._users_by_email[email_n] = user.id
        return user

    def verify_email(self, user_id: str) -> None:
        """Verificar email de un usuario"""
        user = self.get_user(user_id)
        user.is_email_verified = True
        user.mark_updated()

    def login(
        self,
        username_or_email: str,
        plain_password: str,
        ip_address: Optional[str] = None,
    ) -> str:
        """
        Autenticar usuario y crear sesión

        Args:
            username_or_email: Usuario o email
            plain_password: Contraseña
            ip_address: Dirección IP del cliente

        Returns:
            Token de sesión

        Raises:
            ValueError: Si credenciales inválidas o usuario bloqueado
        """
        user = self.find_by_username_or_email(username_or_email)
        if user is None:
            # No revelar si el usuario existe
            raise ValueError("Credenciales inválidas.")

        if not user.can_login():
            raise ValueError(
                "Usuario no puede iniciar sesión (inactivo, eliminado o bloqueado).")

        if not self.hasher.verify_password(plain_password, user.password_hash):
            user.failed_login_attempts += 1
            user.mark_updated()

            if user.failed_login_attempts >= self.max_failed_attempts:
                user.locked_until = now_utc() + self.lock_duration
                user.failed_login_attempts = 0
                user.mark_updated()
                raise ValueError(
                    "Demasiados intentos. Cuenta bloqueada temporalmente.")

            raise ValueError("Credenciales inválidas.")

        # Login exitoso
        user.locked_until = None
        user.failed_login_attempts = 0
        user.last_login_at = now_utc()
        user.last_login_ip = ip_address
        user.mark_updated()

        token = secrets.token_urlsafe(32)
        expires_at = now_utc() + self.session_duration
        self._sessions[token] = (user.id, expires_at)
        return token

    def logout(self, token: str) -> None:
        """Cerrar sesión"""
        self._sessions.pop(token, None)

    def authenticate(self, token: str) -> Optional[UsuarioAvanzado]:
        """
        Autenticar con un token de sesión

        Args:
            token: Token de sesión

        Returns:
            UsuarioAvanzado si token es válido, None si no
        """
        data = self._sessions.get(token)
        if not data:
            return None

        user_id, expires_at = data
        if expires_at <= now_utc():
            self._sessions.pop(token, None)
            return None

        return self._users_by_id.get(user_id)

    def change_password(self, user_id: str, old_password: str, new_password: str) -> None:
        """Cambiar contraseña de usuario"""
        user = self.get_user(user_id)

        if not self.hasher.verify_password(old_password, user.password_hash):
            raise ValueError("La contraseña antigua es incorrecta.")

        user.password_hash = self.hasher.hash_password(new_password)
        user.mark_updated()

    def reset_password_admin(self, user_id: str, new_password: str) -> None:
        """Reiniciar contraseña por admin (sin validar la antigua)"""
        user = self.get_user(user_id)
        user.password_hash = self.hasher.hash_password(new_password)
        user.mark_updated()

    # ---------- Ciclo de vida de usuario ----------

    def deactivate_user(self, user_id: str) -> None:
        """Desactivar usuario"""
        user = self.get_user(user_id)
        user.is_active = False
        user.mark_updated()

    def activate_user(self, user_id: str) -> None:
        """Activar usuario"""
        user = self.get_user(user_id)
        user.is_active = True
        user.mark_updated()

    def soft_delete_user(self, user_id: str) -> None:
        """Borrado lógico de usuario (soft delete)"""
        user = self.get_user(user_id)
        user.deleted_at = now_utc()
        user.is_active = False
        user.mark_updated()

    # ---------- Roles y permisos ----------

    def add_role(self, user_id: str, role: str) -> None:
        """Agregar rol a usuario"""
        user = self.get_user(user_id)
        user.roles.add(role)
        user.mark_updated()

    def remove_role(self, user_id: str, role: str) -> None:
        """Remover rol de usuario"""
        user = self.get_user(user_id)
        user.roles.discard(role)
        user.mark_updated()

    def grant_permission(self, user_id: str, perm: str) -> None:
        """Otorgar permiso a usuario"""
        user = self.get_user(user_id)
        user.permissions.add(perm)
        user.mark_updated()

    def revoke_permission(self, user_id: str, perm: str) -> None:
        """Revocar permiso de usuario"""
        user = self.get_user(user_id)
        user.permissions.discard(perm)
        user.mark_updated()

    def has_permission(self, user_id: str, perm: str) -> bool:
        """
        Verificar si usuario tiene permiso
        Regla simple: permiso directo o rol admin
        """
        user = self.get_user(user_id)
        return perm in user.permissions or "admin" in user.roles

    # ---------- Helpers de búsqueda ----------

    def get_user(self, user_id: str) -> UsuarioAvanzado:
        """Obtener usuario por ID"""
        user = self._users_by_id.get(user_id)
        if user is None:
            raise ValueError("Usuario no encontrado.")
        return user

    def find_by_username_or_email(self, value: str) -> Optional[UsuarioAvanzado]:
        """Buscar usuario por nombre de usuario o email"""
        v = value.strip().lower()
        user_id = self._users_by_username.get(v) or self._users_by_email.get(v)
        return self._users_by_id.get(user_id) if user_id else None

    def get_all_users(self) -> list[UsuarioAvanzado]:
        """Obtener todos los usuarios activos"""
        return [u for u in self._users_by_id.values() if u.deleted_at is None]

    def get_stats(self) -> dict:
        """Obtener estadísticas del sistema"""
        usuarios = self.get_all_users()
        return {
            "total_usuarios": len(usuarios),
            "usuarios_activos": sum(1 for u in usuarios if u.is_active),
            "usuarios_verificados": sum(1 for u in usuarios if u.is_email_verified),
            "usuarios_bloqueados": sum(1 for u in usuarios if u.is_locked()),
            "sesiones_activas": len(self._sessions),
        }


# -------------------------
# DEMOSTRACIÓN Y USO
# -------------------------

if __name__ == "__main__":
    print("=" * 90)
    print("SISTEMA AVANZADO DE GESTIÓN DE USUARIOS")
    print("=" * 90)

    # Crear gestor
    manager = GestorUsuarios()

    # --- Registro de usuarios ---
    print("\n📝 REGISTRO DE USUARIOS:")
    print("-" * 90)

    user1 = manager.register_user(
        username="carlos",
        email="carlos@example.com",
        plain_password="MiContraseñaSegura123",
        full_name="Carlos Báez",
        phone="555-1234",
        roles={"user"},
    )
    print(f"✓ Usuario registrado: {user1.username}")

    user2 = manager.register_user(
        username="juan",
        email="juan@example.com",
        plain_password="OtraContraseñaSegura456",
        full_name="Juan Pérez",
        roles={"user", "moderator"},
    )
    print(f"✓ Usuario registrado: {user2.username}")

    user3 = manager.register_user(
        username="admin",
        email="admin@example.com",
        plain_password="AdminContraseña789Segura",
        full_name="Administrador del Sistema",
        roles={"admin"},
    )
    print(f"✓ Usuario registrado: {user3.username} (Rol: admin)")

    # --- Verificación de email ---
    print("\n✉️ VERIFICACIÓN DE EMAIL:")
    print("-" * 90)
    manager.verify_email(user1.id)
    print(f"✓ Email verificado para {user1.username}")

    # --- Login ---
    print("\n🔐 AUTENTICACIÓN Y SESIONES:")
    print("-" * 90)

    token1 = manager.login(
        "carlos", "MiContraseñaSegura123", ip_address="192.168.1.100")
    print(f"✓ Login exitoso para {user1.username}")
    print(f"  Token: {token1[:20]}...")

    current_user = manager.authenticate(token1)
    print(f"✓ Autenticado como: {current_user.username}")
    print(f"  Último login: {current_user.last_login_at}")
    print(f"  IP: {current_user.last_login_ip}")

    # --- Intentos fallidos de login ---
    print("\n❌ INTENTOS FALLIDOS DE LOGIN:")
    print("-" * 90)

    try:
        for intento in range(1, 6):
            manager.login("juan", "ContraseñaIncorrecta")
    except ValueError as e:
        print(f"✗ Intento {intento}: {e}")
        user_bloqueado = manager.get_user(user2.id)
        print(f"  Usuario bloqueado hasta: {user_bloqueado.locked_until}")

    # --- Cambio de contraseña ---
    print("\n🔑 CAMBIO DE CONTRASEÑA:")
    print("-" * 90)

    manager.change_password(
        user1.id,
        "MiContraseñaSegura123",
        "NuevaContraseñaSegura999"
    )
    print(f"✓ Contraseña cambiada para {user1.username}")

    manager.logout(token1)
    print(f"✓ Sesión cerrada")

    token1_new = manager.login(
        "carlos", "NuevaContraseñaSegura999", ip_address="192.168.1.101")
    print(f"✓ Login exitoso con nueva contraseña")

    # --- Roles y permisos ---
    print("\n🔰 ROLES Y PERMISOS:")
    print("-" * 90)

    manager.add_role(user1.id, "moderator")
    print(f"✓ Rol 'moderator' agregado a {user1.username}")
    print(f"  Roles actuales: {user1.roles}")

    manager.grant_permission(user1.id, "edit_posts")
    manager.grant_permission(user1.id, "delete_comments")
    print(f"✓ Permisos otorgados: {user1.permissions}")

    print(f"✓ ¿{user1.username} puede editar posts? {manager.has_permission(user1.id, 'edit_posts')}")
    print(
        f"✓ ¿{user1.username} es admin? {manager.has_permission(user1.id, 'admin_access')}")
    print(
        f"✓ ¿{user3.username} es admin? {manager.has_permission(user3.id, 'admin_access')}")

    # --- Información de usuarios ---
    print("\n👥 INFORMACIÓN DE USUARIOS:")
    print("-" * 90)

    for usuario in manager.get_all_users():
        print(f"  {usuario.get_info()}")

    # --- Estadísticas ---
    print("\n📊 ESTADÍSTICAS DEL SISTEMA:")
    print("-" * 90)

    stats = manager.get_stats()
    for clave, valor in stats.items():
        print(f"  {clave.replace('_', ' ').title()}: {valor}")

    # --- Gestión de usuarios ---
    print("\n⚙️ GESTIÓN DE USUARIOS:")
    print("-" * 90)

    manager.deactivate_user(user2.id)
    print(f"✓ Usuario {user2.username} desactivado")

    manager.activate_user(user2.id)
    print(f"✓ Usuario {user2.username} reactivado")

    manager.soft_delete_user(user2.id)
    print(f"✓ Usuario {user2.username} eliminado (soft delete)")

    print("\n" + "=" * 90)
    print("FIN DE LA DEMOSTRACIÓN")
    print("=" * 90)
