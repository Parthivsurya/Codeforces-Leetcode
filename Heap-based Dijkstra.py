import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]  
    while pq:
        current_dist, u = heapq.heappop(pq)
        if current_dist > dist[u]:
            continue
        for v, weight in graph[u]:
            new_dist = dist[u] + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))
    return dist

def bellman_ford(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u]:
                if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
    for u in graph:
        for v, weight in graph[u]:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                raise ValueError("Graph contains a negative weight cycle")
    return dist