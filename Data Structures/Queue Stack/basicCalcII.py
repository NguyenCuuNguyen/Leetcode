class Solution:
    def calculate(self, s: str) -> int:
        stack, num, prevOp = [], 0, "+"
        for i in range(len(s)):
            if s[i].isdigit(): 
                num = num * 10 + int(s[i]) #*10 in case number >= 10: 11 * 5 + 2, num = 11
            if s[i] in "+-*/" or i == len(s) -1: #cannot be elif here bc when reach the end, would miss last operator
                if prevOp == "+": #take care of first num
                    stack.append(num) #stack of number to be summed in return
                elif prevOp == "-":
                    stack.append(-num)
                elif prevOp == "*":
                    stack.append(stack.pop() * num) #pop 11 => 11*5 => append(55)
                else:
                    stack.append(int(stack.pop()/ num))
                num = 0
                prevOp = s[i] #retrospectively save the operator  
        return sum(stack)
