N= int(input())
b = list(map(int, input().split()))
balloons = list(range(1, N + 1))
idx = 0

while b:
    num = b.pop(idx)
    print(balloons.pop(idx), end=' ')

    if not b:
        break
    if num > 0:
        idx = (idx + (num - 1)) % len(b)
    else:
        idx = (idx + num) % len(b)
