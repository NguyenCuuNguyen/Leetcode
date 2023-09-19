class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0]*k #initialization turns out to be important...
        self.len = 0
        self.capacity = k;
        self.front = self.rear = -1 #index of front, rear
        
    def enQueue(self, value: int) -> bool:
        #true on success enqueue:
        if self.isFull():
            return False
        else:
            if self.rear == -1:
                self.rear = self.front = 0
            else:
                self.rear = (self.rear+1) % self.capacity
            self.q[self.rear]=value 
            self.len += 1
            return True
            
    def deQueue(self) -> bool: #Failed to dequeue(1)
        if self.isEmpty(): return False
        if self.front == self.rear: #1 element left
            self.rear = self.front = -1
        else:
            self.front = (self.front + 1) % self.capacity
        self.len -= 1
            #self.q[next] = value
        return True
            
    def Front(self) -> int:
        # if self.front == self.rear:
        #     return -1
        # else:
        return self.q[self.front] if self.len != 0 else -1
        
    def Rear(self) -> int:
        return self.q[self.rear] if self.len != 0 else -1
        # if self.isEmpty():
        #     return -1
        # else:
        #     return self.q[self.rear]
        
    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.capacity
        # if self.rear != -1 and self.front != -1:
        #     #if (self.rear+1) % self.size == self.front:
        #     next = (self.rear+1) % self.size
        #     if self.q[next] == self.front:
        #         return True
        #     else:
        #         return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
