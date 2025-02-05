class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack():
    def __init__(self):
        self.top = None

    def push(self, val):
        new_top = Node(val)
        new_top.next = self.top
        self.top = new_top

    def pop(self):
        if self.top is None:
            return None
        val = self.top.val
        self.top = self.top.next
        return val

    def peek(self):
        if self.top is None:
            return None
        return self.top.val

    def isEmpty(self):
        return self.top is None


stack = Stack()
stack.push(10)
stack.push(20)
print(stack.peek())
print(stack.pop())
print(stack.isEmpty())
print(stack.pop())
print(stack.isEmpty())