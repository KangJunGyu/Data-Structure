class SearchGraph():
    def __init__(self, num_node):
        self.num_node = num_node
        self.graph = [[0 for _ in range(num_node)] for _ in range(num_node)]

    def insert(self, node, target):
        self.graph[node - 1][target - 1] = 1
        self.graph[target - 1][node - 1] = 1

    def dfs(self, start, visited):
        visited[start - 1] = True
        print(start, end=' ')

        for i in range(len(self.graph)):
            if self.graph[start - 1][i] == 1 and not visited[i]:
                self.dfs(i + 1, visited)
    def bfs(self, start, visited):
        queue = [start]
        visited[start - 1] = True
        while queue:
            v = queue.pop(0)
            print(v, end=' ')

            for i in range(len(self.graph[v - 1])):
                if self.graph[v - 1][i] == 1 and not visited[i]:
                    queue.append(i + 1)
                    visited[i] = True



N, M, V = map(int, input().split())
g = SearchGraph(N)

for _ in range(M):
    node, target = map(int, input().split())
    g.insert(node, target)

dfsvisited = [False] * N
bfsvisited = [False] * N


g.dfs(V, dfsvisited)
print()
g.bfs(V, bfsvisited)