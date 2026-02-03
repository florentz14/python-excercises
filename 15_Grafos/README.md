# 15_Grafos (Graphs)

Grafos: **lista de adyacencia**, matriz de adyacencia, BFS, DFS, caminos, Dijkstra, ciclos, orden topológico, MST.

| Archivo | Contenido |
|---------|-----------|
| `grafo_01_lista_adyacencia.py` | Grafo como dict (vértice → lista de adyacentes) |
| `grafo_02_clase.py` | Clase Grafo: add_vertice(), add_arista(), adyacentes() |
| `grafo_03_bfs.py` | BFS (recorrido en anchura con cola) |
| `grafo_04_dfs.py` | DFS (recorrido en profundidad con recursión) |
| `grafo_05_lista_adyacencia.py` | GrafoListaAdyacencia: dirigido/no, BFS, DFS, DFS iterativo |
| `grafo_06_matriz_adyacencia.py` | GrafoMatrizAdyacencia: representación con matriz |
| `grafo_07_busqueda_caminos.py` | GrafoCompleto: buscar_camino, todos_los_caminos, componentes_conexas |
| `grafo_08_dijkstra.py` | Dijkstra: distancias mínimas desde un nodo |
| `grafo_09_deteccion_ciclos.py` | Detección de ciclos (dirigido y no dirigido) |
| `grafo_10_ordenamiento_topologico.py` | Ordenamiento topológico (DAG) |
| `grafo_11_ponderado_completo.py` | GrafoPonderado: camino_minimo, arbol_expansion_minima (Prim) |
| `grafo_12_resumen.py` | Resumen: representaciones, algoritmos, aplicaciones |

**Dependencias:** 07, 08, 09, 10 y 11 importan `GrafoListaAdyacencia` desde `grafo_05_lista_adyacencia`. Ejecutar desde la carpeta `15_Grafos` o desde la raíz (`python 15_Grafos/grafo_XX.py`).

```bash
cd 15_Grafos
python grafo_05_lista_adyacencia.py
python grafo_06_matriz_adyacencia.py
python grafo_07_busqueda_caminos.py
python grafo_08_dijkstra.py
python grafo_09_deteccion_ciclos.py
python grafo_10_ordenamiento_topologico.py
python grafo_11_ponderado_completo.py
python grafo_12_resumen.py
```
