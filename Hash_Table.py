class HashNode():
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next

class HashTable():
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def _hash_function(self, key):
        return hash(key) % self.size

    def put(self, key, val):
        idx = self._hash_function(key)
        if self.table[idx] is None:
            self.table[idx] = HashNode(key, val)
        else:
            node = self.table[idx]
            while node is not None:
                if node.key == key: # 중복 키가 들어오는 경우
                    node.val = val
                    return
                if node.next is None:
                    break
                node = node.next
            node.next = HashNode(key, val)

    def get(self, key):
        idx = self._hash_function(key)
        node = self.table[idx]
        while node is not None:
            if node.key == key:
                return node.val
            node = node.next # Chaining 된 경우
        return None

    def remove(self, key):
        idx = self._hash_function(key)
        node = self.table[idx]
        prev_node = None
        while node is not None:
            if node.key == key:
                if prev_node is None:
                    self.table[idx] = node.next  # 첫번째 노드 삭제
                else:
                    prev_node.next = node.next  # 중간 노드 삭제
                return True
            prev_node = node
            node = node.next
        return False


ht = HashTable()
ht.put(1, "강준규")
ht.put(2, "성나영")
ht.put(8, "이원호")

print(ht.get(1))
print(ht.get(2))
print(ht.get(8))
print(ht.get(5))

# 데이터 삭제
ht.remove(2)
print(ht.get(2))