# 19_Tablas_Hash

Estructuras de datos de tablas hash (Hash Tables).

## Archivos

| Archivo | Contenido |
|---------|-----------|
| `01_hash_table_chaining.py` | Tabla hash con encadenamiento (listas enlazadas) |
| `02_hash_table_open_addressing.py` | Tabla hash con direccionamiento abierto (linear probing) |
| `03_hash_functions.py` | Funciones hash comunes (division, multiplication, DJB2, FNV-1a) |
| `04_hash_table_applications.py` | Aplicaciones prácticas (word frequency, two sum, LRU cache) |

## Conceptos

### Tabla Hash
```
Key -> Hash Function -> Index -> Value

┌─────┬─────────────┐
│  0  │  (k1, v1)   │
│  1  │    empty    │
│  2  │  (k2, v2)   │
│  3  │  (k3, v3)   │
│ ... │    ...      │
└─────┴─────────────┘
```

### Manejo de Colisiones

**Encadenamiento (Chaining):**
```
[0] -> (k1,v1) -> (k4,v4) -> None
[1] -> (k2,v2) -> None
[2] -> (k3,v3) -> None
```

**Direccionamiento Abierto (Open Addressing):**
```
Colisión en índice i -> probar i+1, i+2, ...
```

## Operaciones

| Operación | Promedio | Peor caso |
|-----------|----------|-----------|
| Insertar | O(1) | O(n) |
| Buscar | O(1) | O(n) |
| Eliminar | O(1) | O(n) |

## Aplicaciones

- Diccionarios y mapas
- Cachés (LRU, LFU)
- Detección de duplicados
- Conteo de frecuencia
- Índices de bases de datos
