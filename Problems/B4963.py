from collections import deque

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

while True:
    mapcnt = 0
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    islandMap = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if islandMap[i][j] == 1 and not visited[i][j]:
                queue = deque([(i, j)])
                visited[i][j] = True
                mapcnt += 1

                while queue:
                    x, y = queue.popleft()

                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < h and 0 <= ny < w and islandMap[nx][ny] == 1 and not visited[nx][ny]:
                            queue.append((nx, ny))
                            visited[nx][ny] = True

    print(mapcnt)