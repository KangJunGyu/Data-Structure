from collections import deque

N, M = map(int, input().split())
miro = [list(map(int, input())) for _ in range(N)]
'''
2차원 배열 받을 때 map(int, input().split())으로 받으면 out of index가 나온다.
입력받을 때 공백없이 한줄로 이어서 받기 때문.
'''
queue = deque([(0, 0)])
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while queue:
    x, y = queue.popleft()

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and miro[nx][ny] == 1:
            miro[nx][ny] = miro[x][y] + 1
            queue.append((nx, ny))

print(miro[N-1][M-1])


