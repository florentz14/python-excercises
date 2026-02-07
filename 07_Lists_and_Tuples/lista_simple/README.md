# Lista Simple - Metodos y Operaciones

Coleccion de archivos individuales que demuestran cada metodo y operacion
de las listas en Python. Cada archivo es independiente y ejecutable por separado.

## Archivos

| # | Archivo | Tema | Metodo/Concepto |
|---|---------|------|-----------------|
| 01 | `01_crear_lista.py` | Crear una lista | `[]`, `list()` |
| 02 | `02_acceso_indices.py` | Acceso por indices | `lista[i]`, `lista[-i]` |
| 03 | `03_longitud.py` | Longitud de lista | `len()` |
| 04 | `04_slicing.py` | Rebanado / Slicing | `lista[i:j]`, `lista[::paso]` |
| 05 | `05_modificar_elementos.py` | Modificar elementos | `lista[i] = val`, `lista[i:j] = [...]` |
| 06 | `06_append.py` | Agregar al final | `lista.append()` |
| 07 | `07_insert.py` | Insertar en posicion | `lista.insert()` |
| 08 | `08_remove.py` | Eliminar por valor | `lista.remove()` |
| 09 | `09_pop.py` | Eliminar y retornar | `lista.pop()` |
| 10 | `10_del.py` | Eliminar con del | `del lista[i]` |
| 11 | `11_loop_for.py` | Recorrer con for | `for x in lista`, `enumerate()` |
| 12 | `12_loop_range.py` | Recorrer con indices | `for i in range(len())` |
| 13 | `13_filtrado_loop.py` | Filtrado con bucle | `for` + `if` + `append()` |
| 14 | `14_list_comprehension.py` | List Comprehension | `[expr for x in lista if cond]` |
| 15 | `15_sort.py` | Ordenar lista | `lista.sort()`, `sorted()` |
| 16 | `16_reverse.py` | Invertir lista | `lista.reverse()`, `reversed()` |
| 17 | `17_copy.py` | Copiar listas | `copy()`, `list()`, `[:]`, `deepcopy` |
| 18 | `18_concatenar.py` | Concatenar con + | `lista1 + lista2`, `*` |
| 19 | `19_join_append_loop.py` | Unir con bucle | `for` + `append()` |
| 20 | `20_extend.py` | Extender lista | `lista.extend()` |
| 21 | `21_count.py` | Contar ocurrencias | `lista.count()` |
| 22 | `22_index.py` | Buscar posicion | `lista.index()` |
| 23 | `23_clear.py` | Vaciar lista | `lista.clear()` |
| 24 | `24_min_max_sum.py` | Min, Max, Suma | `min()`, `max()`, `sum()` |
| 25 | `25_in_membership.py` | Operador in | `in`, `not in` |

## Metodos de Lista - Resumen Rapido

### Agregar elementos
| Metodo | Descripcion | Ejemplo |
|--------|-------------|---------|
| `append(x)` | Agrega al final | `[1,2].append(3)` -> `[1,2,3]` |
| `insert(i,x)` | Inserta en posicion i | `[1,3].insert(1,2)` -> `[1,2,3]` |
| `extend(iter)` | Agrega cada elemento | `[1].extend([2,3])` -> `[1,2,3]` |

### Eliminar elementos
| Metodo | Descripcion | Retorna |
|--------|-------------|---------|
| `remove(x)` | Elimina primera ocurrencia | None |
| `pop(i)` | Elimina por indice | El elemento |
| `clear()` | Vacia la lista | None |
| `del lista[i]` | Elimina por indice | - |

### Buscar y contar
| Metodo | Descripcion |
|--------|-------------|
| `index(x)` | Retorna indice de primera ocurrencia |
| `count(x)` | Retorna cantidad de ocurrencias |
| `x in lista` | Retorna True/False |

### Ordenar y organizar
| Metodo | Descripcion | Modifica original |
|--------|-------------|-------------------|
| `sort()` | Ordena la lista | Si |
| `sorted()` | Retorna copia ordenada | No |
| `reverse()` | Invierte el orden | Si |
| `reversed()` | Retorna iterador invertido | No |

### Copiar
| Metodo | Tipo de copia |
|--------|---------------|
| `copy()` | Superficial (shallow) |
| `list(x)` | Superficial (shallow) |
| `x[:]` | Superficial (shallow) |
| `deepcopy(x)` | Profunda (deep) |

## Como ejecutar

Cada archivo se puede ejecutar de forma independiente:

```bash
python 01_crear_lista.py
python 15_sort.py
```

## Requisitos

- Python 3.x
- No requiere librerias externas
