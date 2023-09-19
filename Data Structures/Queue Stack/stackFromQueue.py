from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque()
        #q2 only stores the latest insert
        # self.q1 = deque()
        # self.q2 = deque()

        #add from the left
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        # self.q2.append(x)
        # if len(self.q1) != 0:
        #     while(len(self.q1) != 0):
        #         self.q2.append(self.q1.popleft())
        # self.q1 = self.q2 
        # self.q2 = []
        temp = deque([x]) #create a new queue
        temp.extend(self.q) #add multiple values at the right end 
        self.q = temp
        
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        # if len(self.q2) != 0:
        #     return self.q2.pop()
        # else:
        return self.q.popleft()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        
        return self.q[0]
        # else:
        #     return self.q1[0]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
