import sys
input = sys.stdin.readline

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        child = len(self.heap) - 1
        parent = (child - 1) // 2

        while child > 0 and self.heap[parent] < self.heap[child]:
            self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
            child = parent
            parent = (child - 1) // 2

    def extract(self):
        if len(self.heap) == 0:
            return 0
        if len(self.heap) == 1:
            return self.heap.pop()

        rtn_val = self.heap[0]
        self.heap[0] = self.heap.pop()

        parent = 0
        while True:
            left_child = 2 * parent + 1
            right_child = 2 * parent + 2
            max_idx = parent

            if left_child < len(self.heap) and self.heap[left_child] > self.heap[max_idx]:
                max_idx = left_child
            if right_child < len(self.heap) and self.heap[right_child] > self.heap[max_idx]:
                max_idx = right_child

            if max_idx == parent:
                break

            self.heap[parent], self.heap[max_idx] = self.heap[max_idx], self.heap[parent]
            parent = max_idx

        return rtn_val


# 명령어 처리
N = int(input())
mh = MaxHeap()

for _ in range(N):
    x = int(input())
    if x == 0:
        print(mh.extract())
    else:
        mh.insert(x)
