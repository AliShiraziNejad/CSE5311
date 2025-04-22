# Implementation and Testing of Graph Algorithms

# 1. Topological Sort and Depth-First Search (DFS)

class Graph:
    def __init__(self, vertices):
        # Initialize adjacency list
        self.vertices = vertices
        self.adj = {}
        for v in vertices:
            self.adj[v] = []

    def add_edge(self, u, v):
        # Add directed edge u -> v
        self.adj[u].append(v)


def dfs_util(graph, v, visited, order):
    visited.add(v)
    order.append(v)
    for neighbor in graph.adj[v]:
        if neighbor not in visited:
            dfs_util(graph, neighbor, visited, order)


def dfs(graph):
    visited = set()
    order = []
    for v in graph.vertices:
        if v not in visited:
            dfs_util(graph, v, visited, order)
    return order


def topological_sort(graph):
    visited = set()
    stack = []

    def visit(v):
        visited.add(v)
        for n in graph.adj[v]:
            if n not in visited:
                visit(n)
        # Prepend v to the stack
        stack.insert(0, v)

    for v in graph.vertices:
        if v not in visited:
            visit(v)
    return stack


# 2. Kruskal's Algorithm for Minimum Spanning Tree (MST)

class DisjointSet:
    def __init__(self, vertices):
        self.parent = {}
        self.rank = {}
        for v in vertices:
            self.parent[v] = v
            self.rank[v] = 0

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1
        return True


def kruskal(vertices, edges):
    ds = DisjointSet(vertices)
    mst = []
    total_weight = 0
    # Sort edges by weight
    sorted_edges = sorted(edges, key=lambda edge: edge[2])
    for edge in sorted_edges:
        u, v, w = edge
        if ds.union(u, v):
            mst.append((u, v, w))
            total_weight += w
    return mst, total_weight


# Testing on classic textbook examples

# Example for Topological Sort & DFS (from CLRS)
vertices_ts = [5, 4, 2, 3, 1, 0]
g = Graph(vertices_ts)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

dfs_order = dfs(g)
topo_order = topological_sort(g)

# Example for Kruskal's MST (from CLRS)
vertices_kruskal = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
edges_kruskal = [
    ('A','B',7), ('A','D',5), ('B','C',8), ('B','D',9),
    ('B','E',7), ('C','E',5), ('D','E',15), ('D','F',6),
    ('E','F',8), ('E','G',9), ('F','G',11)
]
mst_edges, mst_weight = kruskal(vertices_kruskal, edges_kruskal)

# Output results
print("DFS Order on DAG example:", dfs_order)
print("Topological Sort order:", topo_order)
print("MST edges:", mst_edges)
print("Total weight of MST:", mst_weight)
