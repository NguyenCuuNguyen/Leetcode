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


# Time Complexity: O(M + N), where M, N are the lengths of S and T respectively.

# Space Complexity: O(1)O(1)
#Iterate through the string in reverse. If we see a backspace character, the next non-backspace character is skipped. If a character isn't skipped, it is part of the final answer.
import itertools
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s):
            skip = 0
            s = s[::-1] #reverse string
            for char in s:
                if char == "#":
                    skip += 1 
                elif skip: #skip != 0
                    skip -= 1
                else:
                    yield char
            #use yield when we want to iterate over a sequence, but don’t want to store the entire sequence in memory.
        return all(x == y for x, y in itertools.zip_longest(build(s), build(t)))
    #all() function returns True if all items in an iterable are true, otherwise it returns False.
    #itertools.zip_longest: prints the values of iterables alternatively in sequence.

