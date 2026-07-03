class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # maps key to nodes

        # Initialize dummy boundary nodes to avoid handling null checks
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    # Helper function: Remove a node from anywhere in the doubly linked list
    def remove(self, node: Node) -> None:
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    # Helper function: Insert a node at the very right (Most Recently Used position)
    def insert(self, node: Node) -> None:
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Since it was accessed, make it the Most Recently Used item
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        # If the key already exists, delete the old version from the list
        if key in self.cache:
            self.remove(self.cache[key])
            
        # Create a fresh node and add it to the map and MRU position
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)

        # If cache exceeds allowed capacity, evict the Least Recently Used item
        if len(self.cache) > self.cap:
            lru_node = self.left.next
            self.remove(lru_node)
            del self.cache[lru_node.key] # Delete from map

