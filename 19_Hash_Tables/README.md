# 19_Hash_Tables

Estructuras de datos de tablas hash (Hash Tables).

**Run:** `python 01_hash_table_chaining.py` (or any `NN_*.py`) from `19_Hash_Tables/`.

---

## Archivos

| Archivo | Contenido |
|---------|-----------|
| `01_hash_table_chaining.py` | Tabla hash con encadenamiento (listas enlazadas) |
| `02_hash_table_open_addressing.py` | Direccionamiento abierto (linear probing) |
| `03_hash_functions.py` | Funciones hash (division, multiplication, DJB2, FNV-1a) |
| `04_hash_table_applications.py` | Aplicaciones (word frequency, two sum, LRU cache) |
| `05_quadratic_probing.py` | Quadratic probing: i + 1², i + 2²... |
| `06_double_hashing.py` | Double hashing: (h1 + i * h2) % size |
| `07_dynamic_resizing.py` | Load factor, rehashing, resize automático |
| `08_load_factor_analysis.py` | Análisis α = n/m, rendimiento vs load factor |
| `09_hash_set.py` | HashSet (keys only), duplicados, membership |
| `10_custom_hashable_objects.py` | __hash__, __eq__, objetos hashables |
| `11_hash_table_vs_dict.py` | Comparación con dict de Python |
| `12_bloom_filter.py` | Bloom filter, membership probabilístico |

---

## Conceptos

### Resolución de colisiones
- **Chaining:** listas en cada bucket
- **Linear probing:** i+1, i+2, ...
- **Quadratic probing:** i+1², i+2², ...
- **Double hashing:** (h1 + i * h2) % size

### Optimización
- **Load factor** α = n/m
- **Resizing** cuando α > 0.7
- **Rehashing** al expandir

### Operaciones

| Operación | Promedio | Peor caso |
|-----------|----------|-----------|
| Insertar | O(1) | O(n) |
| Buscar | O(1) | O(n) |
| Eliminar | O(1) | O(n) |

---

## Aplicaciones
- Diccionarios y mapas
- Cachés (LRU, LFU)
- Detección de duplicados
- Conteo de frecuencia
- Índices de bases de datos
- Bloom filters (sistemas distribuidos)
