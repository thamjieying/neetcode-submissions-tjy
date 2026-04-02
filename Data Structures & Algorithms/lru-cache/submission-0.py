class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        #self.left = least recently
        # self.right = most recently
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.nxt, self.right.prev = self.right, self.left


    def remove_from_dll(self, node):
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev

    def insert_to_right(self, node):
        prev, nxt = self.right.prev, self.right
        prev.nxt = nxt.prev = node
        node.nxt, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove_from_dll(self.cache[key])
            self.insert_to_right(self.cache[key])
            return self.cache[key].val
        return -1    

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove_from_dll(node)
        self.cache[key] = Node(key, value)
        self.insert_to_right(self.cache[key])

        if len(self.cache) > self.capacity: 
            lru = self.left.nxt
            self.remove_from_dll(lru)
            del self.cache[lru.key]