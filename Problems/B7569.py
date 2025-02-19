from collections import deque

M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

queue = deque()

for h in range(H):
    for x in range(N):
        for y in range(M):
            if tomato[h][x][y] == 1:
                queue.append((h, x, y))

while queue:
    h, x, y = queue.popleft()
    if h + 1 < H and tomato[h + 1][x][y] == 0:
        tomato[h + 1][x][y] = tomato[h][x][y] + 1
        queue.append((h + 1, x, y))

    if h - 1 >= 0 and tomato[h - 1][x][y] == 0:
        tomato[h - 1][x][y] = tomato[h][x][y] + 1
        queue.append((h - 1, x, y))

    if x - 1 >= 0 and tomato[h][x - 1][y] == 0:
        tomato[h][x - 1][y] = tomato[h][x][y] + 1
        queue.append((h, x - 1, y))

    if x + 1 < N and tomato[h][x + 1][y] == 0:
        tomato[h][x + 1][y] = tomato[h][x][y] + 1
        queue.append((h, x + 1, y))

    if y + 1 < M and tomato[h][x][y + 1] == 0:
        tomato[h][x][y + 1] = tomato[h][x][y] + 1
        queue.append((h, x, y + 1))

    if y - 1 >= 0 and tomato[h][x][y - 1] == 0:
        tomato[h][x][y - 1] = tomato[h][x][y] + 1
        queue.append((h, x, y - 1))

day = 0
for i in tomato:
    for j in i:
        if 0 in j:
            print(-1)
            exit(0)

        day = max(day, max(j))

print(day - 1)
