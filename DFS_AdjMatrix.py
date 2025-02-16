def dfs_stack(graph, start, visited):
    stack = [start]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            print(node, end=' ')
            for neighbor in range(len(graph) - 1, 0, -1): #역순
                if graph[node][neighbor] == 1 and not visited[neighbor]:
                    stack.append(neighbor)
def dfs_recursive(graph, node, visited):
    visited[node] = True
    print(node, end=' ')
    for neighbor in range(len(graph)):
        if graph[node][neighbor] == 1 and not visited[neighbor]:
            dfs_recursive(graph, neighbor, visited)

graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6, 7],
    4: [2],
    5: [2],
    6: [3],
    7: [3]
}
graph_matrix = [[0] * 8 for _ in range(8)]
for i in graph:
    for j in graph[i]:
        graph_matrix[i][j] = 1
        graph_matrix[j][i] = 1

visited_stack = [False] * len(graph_matrix)
visited_recursive = [False] * len(graph_matrix)
dfs_stack(graph_matrix, 1, visited_stack)
print()
dfs_recursive(graph_matrix, 1, visited_recursive)
