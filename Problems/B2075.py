import heapq

N = int(input())
min_heap = []

for _ in range(N):
    nums = map(int, input().split())
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > N:
            heapq.heappop(min_heap)

print(min_heap[0])

# heapq.heappushpop(mnh, value)
# enumerate(map(int, sys.stdin.readline().split())) -> 내 입력 두줄을 하나로 합친거(map + for문)