# -------------------------------------------------
# File Name: 43_lookup.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Use dicts as lookup tables (months, status codes, operations).
# -------------------------------------------------

month_names = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

month_num = 3
print(f"Month {month_num}: {month_names.get(month_num, 'Invalid')}")

# Lookup with default
print(f"Month 13: {month_names.get(13, 'Invalid month')}")

# More complex lookup: HTTP status codes
status_codes = {
    200: 'OK',
    201: 'Created',
    301: 'Moved Permanently',
    400: 'Bad Request',
    401: 'Unauthorized',
    403: 'Forbidden',
    404: 'Not Found',
    500: 'Internal Server Error'
}


def get_status_message(code):
    return status_codes.get(code, 'Unknown Status')


print("Status 200:", get_status_message(200))
print("Status 404:", get_status_message(404))
print("Status 999:", get_status_message(999))

# Lookup table for computations
operations = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
    'multiply': lambda x, y: x * y,
    'divide': lambda x, y: x / y if y != 0 else 'Division by zero'
}

op = 'multiply'
result = operations.get(op, lambda x, y: 'Unknown operation')(5, 3)
print(f"5 {op} 3 = {result}")
