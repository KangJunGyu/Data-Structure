class Graph_AdjList:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

gl = Graph_AdjList()
gl.add_edge(1, 2)
gl.add_edge(1, 3)
gl.add_edge(3, 2)
gl.add_edge(4, 1)

for node in gl.graph:
    print(f"{node} -> {gl.graph[node]}")