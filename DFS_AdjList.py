def dfs_stack(graph, start, visited):
    stack = [start]

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            print(node, end=' ')
            stack.extend(reversed(graph[node]))

def dfs_recursive(graph, node, visited):
    visited[node] = True
    print(node, end=' ')

    for neighbor in graph[node]:
        if not visited[neighbor]:
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

visited_stack = [False] * (len(graph) + 1) #1을 더하고, 0번 인덱스 사용 X
visited_recursive = [False] * (len(graph) + 1)
dfs_stack(graph, 1, visited_stack)
print()
dfs_recursive(graph, 1, visited_recursive)