import heapq

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    # 최소 힙을 써야하므로 코스트가 왼쪽, 노드가 오른쪽
    heap = [(0, start)]

    while heap:
        cost, node = heapq.heappop(heap)
        # 이미 더 짧은 거리로 방문한 적이 있다면
        # cost -> 그래프 내 가중치 vs dist[node] -> 최단 거리(출발점 제외 무한으로 초기화)
        if cost > dist[node]:
            continue

        for next_node, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))

    return dist

graph = {
    0: [(1, 2), (2, 5)],
    1: [(2, 1), (3, 3)],
    2: [(3, 2)],
    3: []
}

print(dijkstra(graph, 0))