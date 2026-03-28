class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_map = {} # Hash map to store {key: Node} for O(1) access

        # Initialize dummy head and tail nodes to simplify edge cases
        # head.next will always point to the Most Recently Used (MRU) node
        # tail.prev will always point to the Least Recently Used (LRU) node
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key in self.cache_map:
            node = self.cache_map[key]
            # When a node is accessed, move it to the head (mark as MRU)
            self.remove(node)
            self.set_head(node)
            return node.value
        return -1        

    def put(self, key: int, value: int) -> None:
        if key in self.cache_map:
            # If key exists, update value and move node to the head
            node = self.cache_map[key]
            node.value = value
            self.remove(node)
            self.set_head(node)
        else:
            # If capacity is reached, remove the LRU node (tail.prev)            
            if len(self.cache_map) >= self.capacity:
                del_node = self.tail.prev
                # Remove from hash map using the key stored in the node
                del self.cache_map[del_node.key]
                # Remove from the doubly linked list
                self.remove(del_node)                
            
            # Insert the new node into both hash map and the head of linked list
            new_node = Node(key, value)
            self.cache_map[key] = new_node
            self.set_head(new_node)
            
        
    def remove(self, node):
        """
        Removes a node from its current position in the doubly linked list.
        """        
        node.prev.next = node.next
        node.next.prev = node.prev       
    
    def set_head(self, node):
        """
        Inserts a node immediately after the dummy head.
        """
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)