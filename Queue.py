class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue():
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, val):
        new_node = Node(val)
        if self.rear is None:
            self.rear = new_node
            self.front = self.rear

        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None

        val = self.front.val
        self.front = self.front.next
        if self.front is None: # 해당 value가 큐의 마지막 노드인 경우
            self.rear = None
        return val

    def isEmpty(self):
        return self.front is None


queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
print(queue.dequeue())
print(queue.isEmpty())
print(queue.dequeue())
print(queue.isEmpty())