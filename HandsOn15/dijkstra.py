from typing import Dict, List, Tuple, Set
import heapq

def dijkstra(graph: Dict[str, List[Tuple[str, float]]], source: str) -> Dict[str, float]:
    dist: Dict[str, float] = {v: float('inf') for v in graph}
    dist[source] = 0.0
    visited: Set[str] = set()
    heap: List[Tuple[float, str]] = [(0.0, source)]

    while heap:
        d, u = heapq.heappop(heap)

        if u in visited:
            continue

        visited.add(u)

        for v, w in graph[u]:
            nd = d + w

            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))

    return dist