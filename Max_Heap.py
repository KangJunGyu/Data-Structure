class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        child = len(self.heap) - 1

        while child > 0:
            parent = (child - 1) // 2
            if self.heap[parent] < self.heap[child]:
                self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
                child = parent

            else:
                break

    def extract(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        parent = 0
        rtn_val = self.heap[parent]
        self.heap[parent] = self.heap.pop()

        while parent < len(self.heap):
            left_child = 2 * parent + 1
            right_child = 2 * parent + 2
            max_idx = parent

            if left_child < len(self.heap) and self.heap[left_child] > self.heap[max_idx]:
                max_idx = left_child
            if right_child < len(self.heap) and self.heap[right_child] > self.heap[max_idx]:
                max_idx = right_child

            if parent != max_idx:
                self.heap[parent], self.heap[max_idx] = self.heap[max_idx], self.heap[parent]
                parent = max_idx
            else:
                break

        return rtn_val


mh = MaxHeap()
mh.insert(10)
mh.insert(30)
mh.insert(20)
mh.insert(40)
mh.insert(50)
print(' -> '.join(map(str, mh.heap)))

print("------------")
print(mh.extract())
print("------------")

print(' -> '.join(map(str, mh.heap)))