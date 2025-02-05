class Node ():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class LinkedList ():
    def __init__(self):
        self.head = None

    def append(self, val):
        if self.head is None:
            self.head = Node(val)
            return

        node = self.head
        while node.next is not None:
            node = node.next

        node.next = Node(val)

    def delete(self, val):
        if self.head is None:   # 연결 리스트가 비어있는 경우
            print("List is empty")
            return
        if self.head.val == val: # 삭제하고자 하는 값이 헤드인 경우
            self.head = self.head.next
            print("Head Value is deleted")
            return
        prev = None # 데이터 백업용
        node = self.head
        while node is not None and node.val != val: # 끝까지 가지 않았고, 찾지 못한 경우
            prev = node
            node = node.next
        if node:
            prev.next = node.next
        else: print("Value Error")

    def display(self):
        nodes = [] # list
        node = self.head
        while node:
            nodes.append(str(node.val))
            node = node.next
        print(" -> ".join(nodes))


ll = LinkedList()
ll.append('a')
ll.append('b')
ll.append('c')
ll.display()
ll.delete('b')
ll.display()
ll.delete('d')
ll.display()