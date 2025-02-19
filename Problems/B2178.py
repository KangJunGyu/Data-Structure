from collections import deque

N, M = map(int, input().split())

miro = [list(map(int, input().split())) for _ in range(N)]

queue = deque([(0, 0)])
visited = [[-1] * M for _ in range(N)]
visited[0][0] = 1
while queue:
    x, y = queue.popleft()

