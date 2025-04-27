from dijkstra import dijkstra
from bellman_ford import bellman_ford
from floyd_warshall import floyd_warshall

# page 659 fig 24.6
d_graph = {
    's': [('t', 10), ('y', 5)],
    't': [('x', 1), ('y', 2)],
    'x': [('z', 4)],
    'y': [('t', 3), ('x', 9), ('z', 2)],
    'z': [('s', 7), ('x', 6)]
}

# page 652 fig 24.4
bf_vertices = ['s', 't', 'x', 'y', 'z']
bf_edges = [
    ('s', 't', 6), ('s', 'y', 7),
    ('t', 'x', 5), ('t', 'y', 8), ('t', 'z', -4),
    ('x', 't', -2),
    ('y', 'x', -3), ('y', 'z', 9),
    ('z', 's', 2), ('z', 'x', 7)
]

# page 696 fig 25.4
fw_w = [
    [0, 3, 8, float('inf'), -4],
    [float('inf'), 0, float('inf'), 1, 7],
    [float('inf'), 4, 0, float('inf'), float('inf')],
    [2, float('inf'), -5, 0, float('inf')],
    [float('inf'), float('inf'), float('inf'), 6, 0]
]

print('Dijkstra:', dijkstra(d_graph, 's'))
bf_dist, bf_neg = bellman_ford(bf_vertices, bf_edges, 's')

print('Bellman-Ford:', bf_dist, 'Negative cycle:', bf_neg)
fw_result = floyd_warshall(5, fw_w)

print('Floyd-Warshall:')
for row in fw_result:
    print(row)
