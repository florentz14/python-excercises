# 14_Árboles (Trees)

Estructuras de **árbol binario**, BST, AVL y árbol n-ario.

| Archivo | Contenido |
|---------|-----------|
| `arbol_01_nodo.py` | Clase Nodo y construcción de un árbol |
| `arbol_02_recorrido.py` | Recorridos inorden, preorden, postorden |
| `arbol_03_altura.py` | Altura y tamaño (número de nodos) |
| `arbol_04_binario_basico.py` | NodoArbol, ArbolBinario: insertar, buscar, altura, tamaño |
| `arbol_05_recorridos.py` | ArbolRecorridos: preorden, inorden, postorden, nivel orden (BFS) |
| `arbol_06_bst.py` | ArbolBST: es_bst, encontrar_minimo, encontrar_maximo |
| `arbol_07_avl.py` | ArbolAVL: árbol auto-balanceado con rotaciones |
| `arbol_08_nario.py` | Arbol N-ario: múltiples hijos, DFS y BFS |
| `arbol_09_operaciones.py` | contar_hojas, sumar_valores, es_completo |
| `arbol_10_resumen.py` | Resumen de tipos de árboles y aplicaciones |

**Dependencias entre archivos:** 05 importa de 04; 06 importa de 05; 09 importa de 06. Ejecutar desde la carpeta `14_Arboles` para que los imports funcionen, o desde la raíz: `python 14_Arboles/arbol_04_binario_basico.py` (los que no importan de otros funcionan; para 05, 06, 09 conviene `cd 14_Arboles` y luego `python arbol_XX.py`).

```bash
cd 14_Arboles
python arbol_01_nodo.py
python arbol_04_binario_basico.py
python arbol_05_recorridos.py
python arbol_06_bst.py
python arbol_07_avl.py
python arbol_08_nario.py
python arbol_09_operaciones.py
python arbol_10_resumen.py
```
