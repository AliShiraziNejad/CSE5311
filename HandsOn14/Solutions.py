def depth_first_search(graph):
    time = 0
    color = {u: 'white' for u in graph}
    parent = {u: None for u in graph}
    d = {}
    f = {}
    def dfs_visit(u):
        nonlocal time
        time += 1
        d[u] = time
        color[u] = 'gray'
        for v in graph[u]:
            if color[v] == 'white':
                parent[v] = u
                dfs_visit(v)
        color[u] = 'black'
        time += 1
        f[u] = time

    for u in graph:
        if color[u] == 'white':
            dfs_visit(u)
    return d, f, parent


Dfs_graph = {
    'u': ['v', 'x'],
    'v': ['y'],
    'w': ['y', 'z'],
    'x': ['v'],
    'y': ['x'],
    'z': ['z']
}

d, f, parent = depth_first_search(Dfs_graph)
print("DFS Page 605:")
print("Vertex | Discovery | Finishing | Parent")
for u in sorted(Dfs_graph):
    print(f"  {u}    |    {d[u]}      |    {f[u]}      |   {parent[u]}")


def topological_sort(graph):
    time = 0
    color = {u: 'white' for u in graph}
    f = {}
    topo = []

    def dfs_visit(u):
        nonlocal time
        time += 1
        color[u] = 'gray'
        for v in graph[u]:
            if color[v] == 'white':
                dfs_visit(v)
        color[u] = 'black'
        topo.append(u)
        time += 1
        f[u] = time

    for u in graph:
        if color[u] == 'white':
            dfs_visit(u)

    topo.reverse()
    return topo


Topo_graph = {
    'm': ['q','r','x'],
    'n': ['q','o','u'],
    'o': ['r','s','v'],
    'p': ['o','s','z'],
    'q': ['t'],
    'r': ['v','y'],
    's': ['r'],
    't': ['x'],
    'u': ['t','x'],
    'v': ['w','y'],
    'w': ['z'],
    'x': [],
    'y': [],
    'z': []
}

order = topological_sort(Topo_graph)
print("\nTopological Sort of Page 615:")
print(order)


class DisjointSet:
    def __init__(self, elements):
        self.parent = {e: e for e in elements}
        self.rank = {e: 0 for e in elements}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)

        if rx == ry:
            return False

        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry

        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx

        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        return True


def kruskal(vertices, edges):
    ds = DisjointSet(vertices)
    mst = []
    total_weight = 0
    for u, v, w in sorted(edges, key=lambda e: e[2]):
        if ds.union(u, v):
            mst.append((u, v, w))
            total_weight += w
    return mst, total_weight


vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
edges = [
    ('a', 'b', 4),
    ('a', 'h', 8),
    ('b', 'h', 11),
    ('b', 'c', 8),
    ('c', 'd', 7),
    ('c', 'f', 4),
    ('c', 'i', 2),
    ('d', 'e', 9),
    ('d', 'f', 14),
    ('e', 'f', 10),
    ('f', 'g', 2),
    ('g', 'h', 1),
    ('g', 'i', 6),
    ('h', 'i', 7)
]

mst, weight = kruskal(vertices, edges)
print("\nPage 625:")
print("Edges in MST:")
for u, v, w in mst:
    print(f"({u}, {v}) weight={w}")
print("Total MST weight:", weight)
