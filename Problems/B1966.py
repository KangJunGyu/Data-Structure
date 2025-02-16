N = int(input())
output = []
for _ in range(N):
    cnt = 0
    flg = 0
    n, m = map(int, input().split())
    prior = list(map(int, input().split()))
    while True:
        for i in range(len(prior)):
            if prior[i] == max(prior):
                cnt += 1
                prior[i] = 0
                if i == m:
                    flg = 1
                    break
            else:
                continue
        if flg == 1:
            output.append(cnt)
            break
while output:
    print(output.pop(0))