from collections import deque

def bfs_list(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

def bfs_matrix(graph, start, visited):
    queue = deque([start - 1])
    visited[start - 1] = True

    while queue:
        node = queue.popleft()
        print(node + 1, end=' ')
        for neighbor in range(len(graph)):
            if graph[node][neighbor] and not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6, 7],
    4: [2],
    5: [2],
    6: [3],
    7: [3]
}
graph_matrix = [[0] * 7 for _ in range(7)]
for i in graph:
    for j in graph[i]:
        graph_matrix[i-1][j-1] = 1
        graph_matrix[j-1][i-1] = 1

visited_list = [False] * (len(graph) + 1)
visited_matrix = [False] * (len(graph) + 1)
bfs_list(graph, 1, visited_list)
print()
bfs_matrix(graph_matrix, 1, visited_matrix)
