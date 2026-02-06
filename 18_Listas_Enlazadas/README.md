# 18_Listas_Enlazadas

Estructuras de datos de listas enlazadas (Linked Lists).

## Archivos

| Archivo | Contenido |
|---------|-----------|
| `01_singly_linked_list.py` | Lista enlazada simple (un puntero next) |
| `02_doubly_linked_list.py` | Lista doblemente enlazada (prev y next) |
| `03_circular_linked_list.py` | Lista circular (último apunta al primero) |
| `04_linked_list_operations.py` | Operaciones comunes (reverse, merge, find middle, detect cycle) |

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

## Operaciones

| Operación | Tiempo |
|-----------|--------|
| Acceso por índice | O(n) |
| Insertar al inicio | O(1) |
| Insertar al final | O(n) / O(1)* |
| Buscar | O(n) |
| Eliminar | O(n) |

*O(1) si mantenemos referencia al último nodo
