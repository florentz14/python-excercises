# -------------------------------------------------
# File Name: ITSE-1003/Examples/utils.py
# Author: Florentino Báez
# Date: 3/20/2026
# Description: Shared input validation and utility functions.
# -------------------------------------------------

from typing import Optional
import re
import os
import shutil
from datetime import datetime

def input_int(msg: str, start: Optional[int] = None, end: Optional[int] = None) -> int:
    """Prompt until the user enters a valid integer, optionally within a range."""
    while True:
        prompt = input(msg)
        if not prompt.isdecimal():
            print("Invalid input. Please enter a whole number.")
        elif start is not None and end is not None:
            if not (start <= int(prompt) <= end):
                print(f"Out of range. Enter a number between {start} and {end}.")
            else:
                return int(prompt)
        else:
            return int(prompt)


def input_float(msg: str, start: Optional[float] = None, end: Optional[float] = None) -> float:
    """Prompt until the user enters a valid decimal number, optionally within a range."""
    while True:
        prompt = input(msg)
        try:
            value = float(prompt)
        except ValueError:
            print("Invalid input. Please enter a number (e.g. 3.14).")
            continue
        if start is not None and end is not None:
            if not (start <= value <= end):
                print(f"Out of range. Enter a number between {start} and {end}.")
                continue
        return value


def input_str(msg: str, min_length: int = 1, max_length: Optional[int] = None) -> str:
    """Prompt until the user enters a non-empty string, optionally within a length range."""
    while True:
        prompt = input(msg).strip()
        if len(prompt) < min_length:
            print(f"Too short. Minimum {min_length} character(s) required.")
        elif max_length is not None and len(prompt) > max_length:
            print(f"Too long. Maximum {max_length} characters allowed.")
        else:
            return prompt


def input_yes_no(msg: str) -> bool:
    """Prompt until the user enters y or n. Returns True for yes, False for no."""
    while True:
        prompt = input(msg + " (y/n): ").strip().lower()
        if prompt == "y":
            return True
        elif prompt == "n":
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


def input_option(msg: str, options: list) -> str:
    """Prompt until the user picks one of the given options (case-insensitive)."""
    opts = [str(o).lower() for o in options]
    display = "/".join(str(o) for o in options)
    while True:
        prompt = input(f"{msg} ({display}): ").strip().lower()
        if prompt in opts:
            return prompt
        print(f"Invalid option. Choose from: {display}")


def is_positive_int(value: int) -> bool:
    """Return True if value is a positive integer (> 0)."""
    return isinstance(value, int) and value > 0


def is_non_negative_int(value: int) -> bool:
    """Return True if value is zero or a positive integer (>= 0)."""
    return isinstance(value, int) and value >= 0


def is_positive_float(value: float) -> bool:
    """Return True if value is a positive number (> 0)."""
    return isinstance(value, (int, float)) and value > 0


def clamp(value: float, minimum: float, maximum: float) -> float:
    """Clamp value so it stays within [minimum, maximum]."""
    return max(minimum, min(value, maximum))


# 1. Validación de fechas
def input_date(msg: str, date_format: str = "%Y-%m-%d") -> datetime:
    """Pedir fecha hasta que ingrese una válida."""
    while True:
        date_str = input(msg)
        if is_valid_date(date_str, date_format):
            return datetime.strptime(date_str, date_format)
        print(f"Invalid date format. Please use format: {date_format}")


def is_valid_date(date_str: str, date_format: str = "%Y-%m-%d") -> bool:
    """Verificar si string es fecha válida."""
    try:
        datetime.strptime(date_str, date_format)
        return True
    except ValueError:
        return False


# 2. Validación de email
def input_email(msg: str) -> str:
    """Pedir email hasta que ingrese uno válido."""
    while True:
        email = input(msg).strip()
        if is_valid_email(email):
            return email
        print("Invalid email format. Please enter a valid email address.")


def is_valid_email(email: str) -> bool:
    """Verificar formato de email."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


# 3. Formateo de texto
def format_currency(amount: float, currency: str = "$") -> str:
    """Formatear monto como moneda."""
    return f"{currency}{amount:,.2f}"


def format_phone_number(phone: str) -> str:
    """Formatear número telefónico."""
    # Remover todos los caracteres no numéricos
    digits = re.sub(r'\D', '', phone)
    
    # Formatear según longitud
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    elif len(digits) == 11 and digits[0] == '1':
        return f"+1 ({digits[1:4]}) {digits[4:7]}-{digits[7:]}"
    else:
        return phone  # Devolver original si no coincide


# 5. Utilidades de archivo
def file_exists(filepath: str) -> bool:
    """Verificar si archivo existe."""
    return os.path.exists(filepath)


def backup_file(filepath: str) -> str:
    """Crear backup de archivo."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    # Crear nombre de backup con timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base, ext = os.path.splitext(filepath)
    backup_path = f"{base}_backup_{timestamp}{ext}"
    
    # Copiar archivo
    shutil.copy2(filepath, backup_path)
    return backup_path

def has_valid_avatar(self):
    extensions = ('.jpg', '.jpeg', '.png', '.gif', '.svg')
    return self.avatar_url.lower().endswith(extensions)

def clear_screen():
    """Limpiar pantalla (funciona en Windows y Unix)."""
    os.system('cls' if os.name == 'nt' else 'clear')


def pause(msg: str = "Press Enter to continue..."):
    """Pausar ejecución hasta que el usuario presione Enter."""
    input(msg)


# 6. Utilidades de fecha
def date_diff(date1: datetime, date2: datetime) -> dict:
    """
    Calcular la diferencia entre dos fechas.
    
    Args:
        date1 (datetime): Primera fecha
        date2 (datetime): Segunda fecha
        
    Returns:
        dict: Diccionario con años, meses, días, horas, minutos, segundos
    """
    diff = abs(date2 - date1)
    
    days = diff.days
    seconds = diff.seconds
    
    years = days // 365
    remaining_days = days % 365
    months = remaining_days // 30
    remaining_days = remaining_days % 30
    
    hours = seconds // 3600
    remaining_seconds = seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    
    return {
        'years': years,
        'months': months,
        'days': remaining_days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds,
        'total_days': days,
        'total_seconds': diff.total_seconds()
    }


def human_date_diff(date1: datetime, date2: Optional[datetime] = None) -> str:
    """
    Obtener diferencia entre fechas en formato humano legible.
    
    Args:
        date1 (datetime): Primera fecha
        date2 (datetime): Segunda fecha (default: ahora)
        
    Returns:
        str: Descripción humana de la diferencia
    """
    if date2 is None:
        date2 = datetime.now()
    
    diff = date_diff(date1, date2)
    
    if date2 > date1:
        # Fecha pasada
        if diff['years'] > 0:
            return f"hace {diff['years']} {'año' if diff['years'] == 1 else 'años'}"
        elif diff['months'] > 0:
            return f"hace {diff['months']} {'mes' if diff['months'] == 1 else 'meses'}"
        elif diff['days'] > 0:
            return f"hace {diff['days']} {'día' if diff['days'] == 1 else 'días'}"
        elif diff['hours'] > 0:
            return f"hace {diff['hours']} {'hora' if diff['hours'] == 1 else 'horas'}"
        elif diff['minutes'] > 0:
            return f"hace {diff['minutes']} {'minuto' if diff['minutes'] == 1 else 'minutos'}"
        else:
            return f"hace {diff['seconds']} {'segundo' if diff['seconds'] == 1 else 'segundos'}"
    else:
        # Fecha futura
        if diff['years'] > 0:
            return f"en {diff['years']} {'año' if diff['years'] == 1 else 'años'}"
        elif diff['months'] > 0:
            return f"en {diff['months']} {'mes' if diff['months'] == 1 else 'meses'}"
        elif diff['days'] > 0:
            return f"en {diff['days']} {'día' if diff['days'] == 1 else 'días'}"
        elif diff['hours'] > 0:
            return f"en {diff['hours']} {'hora' if diff['hours'] == 1 else 'horas'}"
        elif diff['minutes'] > 0:
            return f"en {diff['minutes']} {'minuto' if diff['minutes'] == 1 else 'minutos'}"
        else:
            return f"en {diff['seconds']} {'segundo' if diff['seconds'] == 1 else 'segundos'}"


def format_human_date(date: datetime, include_time: bool = True) -> str:
    """
    Formatear fecha en formato humano legible.
    
    Args:
        date (datetime): Fecha a formatear
        include_time (bool): Incluir hora (default: True)
        
    Returns:
        str: Fecha formateada en español
    """
    months = [
        "enero", "febrero", "marzo", "abril", "mayo", "junio",
        "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
    ]
    
    day = date.day
    month = months[date.month - 1]
    year = date.year
    
    if include_time:
        hour = date.hour
        minute = date.minute
        return f"{day} de {month} de {year}, {hour:02d}:{minute:02d}"
    else:
        return f"{day} de {month} de {year}"


def format_relative_date(date: datetime) -> str:
    """
    Formatear fecha relativa al tiempo actual.
    
    Args:
        date (datetime): Fecha a formatear
        
    Returns:
        str: Fecha relativa (hoy, ayer, etc.)
    """
    now = datetime.now()
    today = now.date()
    date_only = date.date()
    
    if date_only == today:
        return f"hoy a las {date.hour:02d}:{date.minute:02d}"
    elif date_only == today.replace(day=today.day - 1):
        return f"ayer a las {date.hour:02d}:{date.minute:02d}"
    elif date_only == today.replace(day=today.day + 1):
        return f"mañana a las {date.hour:02d}:{date.minute:02d}"
    else:
        return human_date_diff(date)