def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    arr = [(0, start)]

    while arr:
        arr.sort(reverse=True)
        cost, node = arr.pop()
        if cost > dist[node]:
            continue

        for next_node, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                arr.append((new_cost, next_node))

    return dist

graph = {
    0: [(1, 2), (2, 5)],
    1: [(2, 1), (3, 3)],
    2: [(3, 2)],
    3: []
}

print(dijkstra(graph, 0))