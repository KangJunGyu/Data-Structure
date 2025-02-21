from collections import deque

M, N = map(int, input().split())

tomato = [list(map(int, input().split())) for _ in range(N)]

queue = deque()

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append((i, j))

while queue:
    x, y = queue.popleft()

    if x > 0 and tomato[x - 1][y] == 0:
        tomato[x - 1][y] = tomato[x][y] + 1
        queue.append((x - 1, y))

    if x < N - 1 and tomato[x + 1][y] == 0:
        tomato[x + 1][y] = tomato[x][y] + 1
        queue.append((x + 1, y))

    if y > 0 and tomato[x][y - 1] == 0:
        tomato[x][y - 1] = tomato[x][y] + 1
        queue.append((x, y - 1))

    if y < M - 1 and tomato[x][y + 1] == 0:
        tomato[x][y + 1] = tomato[x][y] + 1
        queue.append((x, y + 1))

day = 0
flg = 1
for i in tomato:
    if 0 in i:
        flg = 0
    else:
        day = max(day, max(i))

if flg:
    print(day - 1)
else:
    print(-1)