# Time Complexity: O(M + N), where M, N are the lengths of S and T respectively.

# Space Complexity: O(M + N)O(M+N).
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s):
            q = []
            for char in s:
                if char != "#":
                    q.append(char) 
                elif q: #avoid popping from empty list
                    q.pop()
            return "".join(q) #to String
        return build(s) == build(t)
