# Breadth-First Search (BFS) Using Queue

from collections import deque


class Graph:
    """Graph implementation with BFS traversal"""
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, node, neighbor):
        """Adds an edge to the graph"""
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)
    
    def add_undirected_edge(self, node1, node2):
        """Adds an undirected edge (both directions)"""
        self.add_edge(node1, node2)
        self.add_edge(node2, node1)
    
    def bfs(self, start_node):
        """Performs breadth-first search from start_node"""
        if start_node not in self.graph:
            print(f"Node '{start_node}' not found in graph")
            return []
        
        visited = set()
        queue = deque([start_node])
        visited.add(start_node)
        traversal_order = []
        
        print(f"\nBFS starting from node '{start_node}':")
        
        while queue:
            node = queue.popleft()
            traversal_order.append(node)
            print(f"Visiting: {node}")
            
            if node in self.graph:
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
        
        return traversal_order
    
    def find_shortest_path(self, start, end):
        """Finds shortest path using BFS"""
        if start not in self.graph:
            return None
        
        visited = set([start])
        queue = deque([(start, [start])])
        
        while queue:
            node, path = queue.popleft()
            
            if node == end:
                return path
            
            if node in self.graph:
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, path + [neighbor]))
        
        return None


# USAGE EXAMPLES
if __name__ == "__main__":
    print("=" * 60)
    print("BREADTH-FIRST SEARCH (BFS)")
    print("=" * 60)
    
    # Create a directed graph
    graph = Graph()
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('B', 'E')
    graph.add_edge('C', 'F')
    graph.add_edge('E', 'F')
    graph.add_edge('D', 'G')
    graph.add_edge('F', 'G')
    
    print("Graph edges:")
    for node, neighbors in graph.graph.items():
        print(f"  {node} -> {neighbors}")
    
    result = graph.bfs('A')
    print(f"\nTraversal order: {' -> '.join(result)}")
    
    print("\n" + "=" * 60)
    print("SHORTEST PATH EXAMPLE")
    print("=" * 60)
    
    # Create an undirected graph for path finding
    city_graph = Graph()
    city_graph.add_undirected_edge('Home', 'Store')
    city_graph.add_undirected_edge('Home', 'Park')
    city_graph.add_undirected_edge('Store', 'Library')
    city_graph.add_undirected_edge('Park', 'Library')
    city_graph.add_undirected_edge('Library', 'School')
    city_graph.add_undirected_edge('Park', 'Gym')
    city_graph.add_undirected_edge('Gym', 'School')
    
    path = city_graph.find_shortest_path('Home', 'School')
    if path:
        print(f"Shortest path from Home to School: {' -> '.join(path)}")
