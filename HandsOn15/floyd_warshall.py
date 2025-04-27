from typing import List

def floyd_warshall(n: int, w: List[List[float]]) -> List[List[float]]:
    dist = [row[:] for row in w]

    for i in range(n):
        dist[i][i] = 0.0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist