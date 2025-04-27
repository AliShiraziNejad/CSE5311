from typing import Dict, List, Tuple

def bellman_ford(vertices: List[str], edges: List[Tuple[str, str, float]], source: str) -> Tuple[Dict[str, float], bool]:
    dist: Dict[str, float] = {v: float('inf') for v in vertices}
    dist[source] = 0.0

    for _ in range(len(vertices) - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    negative_cycle = False

    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            negative_cycle = True
            break

    return dist, negative_cycle