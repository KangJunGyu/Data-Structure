n, k = map(int, input().split())
p = list(range(1, n + 1))
output = []

idx = 0

while p:
    idx = (idx + k - 1) % len(p) # 순환 큐
    output.append(p.pop(idx))
print("<", end='')
print(', '.join(map(str, output)), end='')
print(">")