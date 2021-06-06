#Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, a#nd empty).

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        #python's list = stack: append(), pop():
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not self.stack1 and self.stack2: #LIFO stack1 is empty and FIFO stack2 has elements
            while self.stack2:
                el = self.stack2.pop()
                self.stack1.append(el)
        self.stack1.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack2 and not self.stack1:
            return None
        if not self.stack2: 
            while self.stack1:
                el = self.stack1.pop()
                self.stack2.append(el)
        return self.stack2.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack2:
            return self.stack2[-1] #return last element
        elif self.stack1:
            return self.stack1[0]
        else:
            return None
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.stack1 == [] and self.stack2 == []
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
