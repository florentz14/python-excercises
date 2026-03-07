# 18_Linked_Lists

Comprehensive linked list algorithms and data structures. From basic implementations to advanced interview problems.

## Archivos

| Archivo                        | Contenido                                                       |
| ------------------------------ | --------------------------------------------------------------- |
| `01_singly_linked_list.py`     | Lista enlazada simple (un puntero next)                         |
| `02_doubly_linked_list.py`     | Lista doblemente enlazada (prev y next)                         |
| `03_circular_linked_list.py`   | Lista circular (último apunta al primero)                       |
| `04_linked_list_operations.py` | Operaciones comunes (reverse, merge, find middle, detect cycle) |
| `05_insert_operations.py`      | Operaciones de inserción (beginning, end, position, after node) |
| `06_delete_operations.py`      | Operaciones de eliminación (head, tail, by value, by position)  |
| `07_reverse_linked_list.py`    | Invertir lista enlazada (iterativo y recursivo)                 |
| `08_find_middle.py`            | Encontrar nodo medio (slow/fast pointers)                       |
| `09_cycle_detection_floyd.py`  | Detectar ciclos (Floyd's Tortoise and Hare)                     |
| `10_merge_two_sorted_lists.py` | Fusionar dos listas ordenadas                                   |
| `11_remove_duplicates.py`      | Eliminar duplicados (ordenada y no ordenada)                    |
| `12_intersection_of_lists.py`  | Encontrar intersección de dos listas                            |
| `13_kth_from_end.py`           | Encontrar k-ésimo nodo desde el final                           |
| `14_partition_list.py`         | Particionar lista alrededor de un valor                         |
| `15_lru_cache_simulation.py`   | Simulación de LRU Cache (lista + hashmap)                       |

## Conceptos

### Lista Enlazada Simple

```
[data|next] -> [data|next] -> [data|next] -> None
```

### Lista Doblemente Enlazada

```
None <- [prev|data|next] <-> [prev|data|next] <-> [prev|data|next] -> None
```

### Lista Circular

```
[data|next] -> [data|next] -> [data|next] --+
     ^                                       |
     +---------------------------------------+
```

## Algoritmos Implementados

| Algoritmo          | Complejidad | Uso                          |
| ------------------ | ----------- | ---------------------------- |
| Reverse List       | O(n)        | Invertir orden de nodos      |
| Find Middle        | O(n)        | Slow/Fast pointers           |
| Cycle Detection    | O(n)        | Floyd's Tortoise and Hare    |
| Merge Sorted Lists | O(m+n)      | Fusionar listas ordenadas    |
| Remove Duplicates  | O(n)        | Hash set para unsorted       |
| Find Intersection  | O(m+n)      | Y-shaped lists               |
| Kth from End       | O(n)        | Two pointers                 |
| Partition          | O(n)        | Reordenar alrededor de pivot |
| LRU Cache          | O(1)        | Cache con lista + hashmap    |

## Operaciones

| Operación          | Tiempo        |
| ------------------ | ------------- |
| Acceso por índice  | O(n)          |
| Insertar al inicio | O(1)          |
| Insertar al final  | O(n) / O(1)\* |
| Buscar             | O(n)          |
| Eliminar           | O(n)          |

\*O(1) si mantenemos referencia al último nodo
