#https://leetcode.com/problems/lru-cache/?envType=daily-question&envId=2023-09-27
#FIRST ATTEMPT: FAILED AT BIG INPUT CASE 16/22 because Output limit exceeded
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [x for x in range(self.capacity)]
        self.counter ={}
        self.cache = {}
        # self.oldest = None

    def get(self, key: int) -> int:
        # Return the value of the key if the key exists, 
        #otherwise return -1.
        #update oldest
        if key not in self.cache:
            return -1
        else:
            # if key not in self.counter:
            #     self.counter[key] = 0
            # self.counter[key] +=1
            self.updateOldest()
            self.counter[key] = 0
            print(f"After get key={key}: cache={self.cache}, counter={self.counter}")
            return self.cache[key]

    def updateOldest(self) -> None:
        for k,v in self.counter.items():
            self.counter[k] -= 1

    def put(self, key: int, value: int) -> None:
        # Update the value of the key if the key exists.
        # Otherwise, add the key-value pair to the cache. 
        #   If the number of keys exceeds the capacity from this operation, evict the least recently used key.
        print(f"Before put key={key}, value={value}: cache={self.cache}, counter={self.counter}")
        # if self.oldest == None: #empty cache 
        self.updateOldest()
        if key in self.cache:
           self.cache[key] = value
           self.counter[key] = 0
        else:
            if len(self.cache) >= self.capacity:  #evict LRU
                tup = min(zip(self.counter.values(), self.counter.keys()))
                print(f"tup={tup}")
                del self.cache[tup[1]]
                del self.counter[tup[1]]
                self.cache[key] = value
                self.counter[key] = 0
            else:
                self.cache[key] = value
                self.counter[key] = 0
        
        print(f"After put: cache={self.cache}, counter={self.counter}")


#ATTEMPT 2: FAILED BECAUSE HEAD.NEXT == NONE

class LRUCache:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None
            

    def __init__(self, capacity: int): #Init 1 head pointing to tail and 1 tail pointing to head
        self.cap = capacity
        self.head = self.Node(-1,-1)
        self.tail = self.Node(-1,-1)
        self.head.next = self.tail
        self.tail.next = self.head
        self.cache = {}

    def delete_node(self, key:int) -> None:
        cur = self.head
        prev = None
        while cur.val != key:
            prev = cur
            cur = cur.next
        prev.next = cur.next
        cur.next.prev = cur.prev
        
    def swap_node(self, node1: Node, node2:Node) -> None:
        temp = self.Node(node1.key, node1.val)
        temp.next = node1.next
        temp.prev = node1.prev
        node1.next = node2.next
        node1.prev = node2.prev
        node2.next = temp.next
        node2.prev = temp.prev

    def get(self, key: int) -> int:
        # Return the value of the key if the key exists, 
        #otherwise return -1.
        #update oldest
        if key not in self.cache:
            # node = self.Node(key)
            return -1 
        else:
            node = self.head.next
            while node.val != key:
                node = node.next
            self.swap_node(node, self.head.next)
        return node

    def put(self, key: int, value: int) -> None:
        # Update the value of the key if the key exists.
        # Otherwise, add the key-value pair to the cache. 
        #   If the number of keys exceeds the capacity from this operation, evict the least recently used key.
        print(f"Before put key={key}, value={value}: cache={self.cache}")
        node = self.get(key)
        if node == -1:
            node = self.Node(key, value)
            self.swap_node(node, self.head.next)
            node = self.head.next
        else:
            if len(self.cache) == self.cap:
                dummy = self.tail.next.prev
                self.delete_node(self.tail.next)
                dummy = self.tail
                self.swap_node(node, self.head.next)
                node = self.head.next
        self.cache[key] = value
        print(f"After put key={key}, value={value}: cache={self.cache}")



#SOLUTION 1: REVIEW THIS 
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class LRUCache:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None
            

    def __init__(self, capacity: int): #Init 1 head pointing to tail and 1 tail pointing to head
        self.cap = capacity
        self.head = self.Node(-1,-1)
        self.tail = self.Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}

    # def __dir__(self):
    #     return self.cache

    def delete_node(self, delNode) -> None:
        prev = delNode.prev
        nex = delNode.next
        prev.next = nex
        nex.prev = prev

    def add_node(self, newNode:Node):
        temp = self.head.next
        newNode.next = temp
        newNode.prev = self.head
        self.head.next = newNode
        temp.prev = newNode

    # def swap_node(self, node1: Node, node2:Node) -> None:
    #     temp = self.Node(node1.key, node1.val)
    #     temp.next = node1.next
    #     temp.prev = node1.prev
    #     node1.next = node2.next
    #     node1.prev = node2.prev
    #     node2.next = temp.next
    #     node2.prev = temp.prev

    def get(self, key: int) -> int:
        # Return the value of the key if the key exists, 
        #otherwise return -1.
        #update oldest
        if key in self.cache:
            node = self.cache[key]
            answer = node.val
            #delete node from old position and add it to head.next
            del self.cache[key]
            self.delete_node(node)
            self.add_node(node)
            self.cache[key] = self.head.next
            return answer
        return -1

    def put(self, key: int, value: int) -> None:
        # Update the value of the key if the key exists.
        # Otherwise, add the key-value pair to the cache. 
        #   If the number of keys exceeds the capacity from this operation, evict the least recently used key.
        if key in self.cache:
            cur = self.cache[key]
            del self.cache[key]
            self.delete_node(cur)
        if len(self.cache) == self.cap:
            del self.cache[self.tail.prev.key]
            self.delete_node(self.tail.prev)
        self.add_node(self.Node(key,value))
        self.cache[key] = self.head.next
        print(f"self.cache={self.cache.__dir__}")