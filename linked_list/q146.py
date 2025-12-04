# 146. LRU Cache

# Difficulty: Medium

# Topics: Hash Table, Linked List, Design, Doubly-Linked List

# Recommended Time & Space Complexity
# You should aim for a solution with O(1) time for each put() and get() 
# function call and an overall space of O(n), where n is the capacity of the LRU cache. 

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to node

        # left=LRU, right=most recent
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:

        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        
        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    lruCache = LRUCache(2)
    print(lruCache.put(1, 10))   # cache: {1=10} -> return None
    print(lruCache.get(1))       # return 10
    print(lruCache.put(2, 20))   # cache: {1=10, 2=20} -> return None
    print(lruCache.put(3, 30))   # cache: {2=20, 3=30}, key=1 was evicted -> return None
    print(lruCache.get(2))       # returns 20 
    print(lruCache.get(1))       # return -1 (not found)
