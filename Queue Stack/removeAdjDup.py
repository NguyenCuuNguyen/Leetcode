#given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

#We repeatedly make duplicate removals on s until we no longer can.

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = ['0']
        for char in s:
            if stack[-1] == char: #duplicate
                stack.pop()#remove(letter)
            else:
                stack.append(char)
        result = ''.join(stack[1:])
        return result
            
