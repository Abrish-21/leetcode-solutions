class ListNode:
    def __init__(self, val = 0, key = 0, next_ptr = None, prev_ptr = None):
        self.key = key
        self.val = val
        self.prev = prev_ptr 
        self.next = next_ptr

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity  = capacity
        self.cache  = {}

        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    def remove(self,node):
        prev_node = node.prev
        next_node = node.next

        next_node.prev = prev_node
        prev_node.next = next_node

   

    def insert(self,node):
        next_node = self.head.next

        self.head.next = node 
        node.prev = self.head
        node.next = next_node
        next_node.prev = node

     


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)  
            return node.val




        
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
            
        else:
            new_node = ListNode(value, key)
            if len(self.cache) >= self.capacity:
                lru = self.tail.prev
                self.remove(lru)
                del self.cache[lru.key]
            self.insert(new_node)
            self.cache[key] = new_node

        

