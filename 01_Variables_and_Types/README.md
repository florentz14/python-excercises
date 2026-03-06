# 01 - Variables and Types

Variables and data types in Python organized in subfolders: basic types, dictionaries,
lists, sets, tuples, operations, and strings.

## Structure

```
01_Variables_and_Types/
|-- data_types/    (14 archivos)  Basic data types
|-- dictionaries/   (16 archivos)  Diccionarios
|-- lists/          (20 archivos)  Listas
|-- sets/           (18 archivos)  Conjuntos (Sets)
|-- tuples/         (14 archivos)  Tuplas
|-- operations/    (9 archivos)   Mathematical operations, arithmetic, etc.
|-- strings/       (4 archivos)   Algoritmos y ejercicios con cadenas
```

## Subcarpetas

### `data_types/` - Basic Data Types (14 archivos)

| # | Archivo | Contenido |
|---|---------|-----------|
| 01 | `01_complex.py` | Numeros complejos |
| 02 | `02_variables.py` | int, float, str, bool |
| 03 | `03_strings.py` | Strings y metodos |
| 04 | `04_comparacion.py` | Operadores de comparacion |
| 05 | `05_tipos.py` | Tipos y conversion |
| 07 | `07_inputs.py` | input(), conversion de entrada |
| 08 | `08_conversion.py` | int(), float(), str(), list(), tuple(), set() |
| 09 | `09_constantes_asignacion.py` | Constantes, asignacion multiple |
| 10 | `10_none.py` | Tipo None |
| 11 | `11_print_sep_end.py` | print(sep=, end=) |
| 12 | `12_membresia.py` | in, not in |
| 13 | `13_logicos.py` | and, or, not, short-circuit |
| 14 | `14_flujos.py` | if/elif/else, for, while |

### `dictionaries/` - Diccionarios (16 archivos)

| # | Archivo | Contenido |
|---|---------|-----------|
| 01 | `01_create_and_display.py` | Crear y mostrar |
| 02 | `02_access_by_key.py` | Acceso por clave |
| 03 | `03_get_method.py` | Metodo get() |
| 04 | `04_add_modify.py` | Agregar y modificar |
| 05 | `05_remove_items.py` | Eliminar elementos |
| 06 | `06_loop.py` | Iterar diccionarios |
| 07 | `07_loop_items.py` | Iterar con items() |
| 08 | `08_keys_values.py` | keys() y values() |
| 09 | `09_check_key_exists.py` | Verificar si existe clave |
| 10 | `10_update.py` | Metodo update() |
| 11 | `11_copy.py` | Copiar diccionario |
| 12 | `12_clear.py` | Limpiar diccionario |
| 13 | `13_nested.py` | Diccionarios anidados |
| 14 | `14_comprehension.py` | Dict comprehension |
| 15 | `15_list_tuples_to_dict.py` | Convertir lista de tuplas |
| 16 | `16_setdefault.py` | Metodo setdefault() |

### `lists/` - Listas (20 archivos)

| # | Archivo | Contenido |
|---|---------|-----------|
| 01 | `01_create_and_display.py` | Crear y mostrar |
| 02 | `02_access_by_index.py` | Acceso por indice |
| 03 | `03_add_elements.py` | append, insert, extend |
| 04 | `04_remove_elements.py` | remove, pop, del |
| 05 | `05_slice.py` | Slicing basico |
| 06 | `06_loop.py` | Iterar con for |
| 07 | `07_comprehension.py` | List comprehension |
| 08 | `08_sort_reverse.py` | sort, reverse |
| 09 | `09_find_and_membership.py` | in, index |
| 10 | `10_operations.py` | Concatenar, repetir |
| 11 | `11_comprehension_avanzado.py` | Comprehension avanzado |
| 12 | `12_ordenar_enumerar_zip.py` | sorted, enumerate, zip |
| 13 | `13_map.py` | map() |
| 14 | `14_filter.py` | filter() |
| 15 | `15_reduce.py` | reduce() |
| 16 | `16_slice_avanzado.py` | Slicing avanzado |
| 17 | `17_pila.py` | Pila (Stack - LIFO) |
| 18 | `18_cola.py` | Cola (Queue - FIFO) |
| 19 | `19_anidadas_copiar.py` | Listas anidadas y copias |
| 20 | `20_any_all_unicos.py` | any, all, unicos |

### `sets/` - Conjuntos (18 archivos)

| # | Archivo | Contenido |
|---|---------|-----------|
| 01 | `01_create_and_display.py` | Crear y mostrar |
| 02 | `02_empty_set.py` | Set vacio vs dict |
| 03 | `03_from_list.py` | Crear desde lista |
| 04 | `04_add_remove.py` | add, remove, discard |
| 05 | `05_membership.py` | in, not in |
| 06 | `06_loop.py` | Iterar set |
| 07 | `07_union.py` | Union (\|) |
| 08 | `08_intersection.py` | Interseccion (&) |
| 09 | `09_difference.py` | Diferencia (-) |
| 10 | `10_symmetric_difference.py` | Diferencia simetrica (^) |
| 11 | `11_subset_superset.py` | issubset, issuperset |
| 12 | `12_clear.py` | clear() |
| 13 | `13_copy.py` | copy() |
| 14 | `14_update.py` | update() |
| 15 | `15_min_max_pop.py` | min, max, pop |
| 16 | `16_comprehension.py` | Set comprehension |
| 17 | `17_unique_elements.py` | Elementos unicos |
| 18 | `18_common_hobbies.py` | Ejemplo practico |

### `tuples/` - Tuplas (14 archivos)

| # | Archivo | Contenido |
|---|---------|-----------|
| 01 | `01_create_and_display.py` | Crear y mostrar |
| 02 | `02_access_by_index.py` | Acceso por indice |
| 03 | `03_negative_indexing.py` | Indices negativos |
| 04 | `04_slice.py` | Slicing |
| 05 | `05_loop.py` | Iterar tuplas |
| 06 | `06_find_and_membership.py` | in, index |
| 07 | `07_count.py` | count() |
| 08 | `08_concatenation_repetition.py` | Concatenar, repetir |
| 09 | `09_unpacking.py` | Desempaquetado |
| 10 | `10_single_element.py` | Tupla de un elemento |
| 11 | `11_immutability.py` | Inmutabilidad |
| 12 | `12_mixed_types.py` | Tipos mixtos |
| 13 | `13_nested.py` | Tuplas anidadas |
| 14 | `14_convert_list_tuple.py` | Conversion lista-tupla |

### `operations/` - Mathematical operations (9 archivos)

| # | Archivo | Contenido |
|---|---------|-----------|
| 01 | `01_two_sum.py` | Encontrar dos indices que sumen el objetivo (target) |
| 02 | `02_aritmeticos.py` | Operadores +, -, *, /, //, %, ** |
| 03 | `03_asignacion_compuesta.py` | Operadores +=, -=, *=, etc. |
| 04 | `04_logicos.py` | Operadores and, or, not |
| 05 | `05_two_sum_v2.py` | Two Sum optimizado (implementacion compacta) |
| 06 | `06_two_sum_bruteforce.py` | Two Sum bruteforce O(n²), sin diccionario |
| 07 | `07_two_sum_numpy.py` | Two Sum con NumPy (basic + matrix) |
| 08 | `08_max_subarray_sum_bruteforce.py` | Max sum subarray size k (bruteforce) |
| 09 | `09_max_subarray_sum_sliding_window.py` | Max sum subarray (sliding window) |

### `strings/` - Algoritmos con cadenas (5 archivos)

| # | Archivo | Contenido |
|---|---------|-----------|
| 01 | `01_valid_palindrome.py` | Comprobar si una cadena es palindromo valido |
| 02 | `02_longest_unique_substring_bruteforce.py` | Substring mas larga sin repetir (bruteforce) |
| 03 | `03_longest_unique_substring_sliding_window.py` | Substring mas larga (sliding window) |
| 04 | `04_longest_unique_substring_dict.py` | Substring mas larga (dict, recomendado) |
| 05 | `05_longest_unique_substring_freq_counter.py` | Substring mas larga (defaultdict) |

## Resumen

| Subcarpeta | Archivos | Tema |
|------------|----------|------|
| `data_types/` | 14 | Basic data types |
| `dictionaries/` | 16 | Diccionarios |
| `lists/` | 20 | Listas |
| `sets/` | 18 | Conjuntos (Sets) |
| `tuples/` | 14 | Tuplas |
| `operations/` | 9 | Mathematical operations |
| `strings/` | 5 | String algorithms |
| **Total** | **95** | |

## Como ejecutar

```bash
cd 01_Variables_and_Types
python data_types/01_complex.py
python dictionaries/01_create_and_display.py
```

## Requisitos

- Python 3.x
- No requiere librerias externas
