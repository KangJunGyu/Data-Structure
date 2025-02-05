class Graph_AdjMatrix:
    def __init__(self, num_node):
        self.num_node = num_node
        self.graph = [[0 for _ in range(num_node)] for _ in range(num_node)] # 2차원 생성

    def add_edge(self, u, v):
        self.graph[u-1][v-1] = 1


gm = Graph_AdjMatrix(4)
gm.add_edge(1, 2)
gm.add_edge(1, 3)
gm.add_edge(3, 2)
gm.add_edge(4, 1)

for g in gm.graph:
    print(g)