#https://leetcode.com/problems/roman-to-integer/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    #SOLUTION 1: O(N) time and space
    def romanToInt(self, s: str) -> int:
        mapp = {'I': 1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        out = 0
        for i in range(len(s)-1):
            if mapp[s[i+1]] > mapp[s[i]]: #exception cases, so subtract
                out -= mapp[s[i]]
            else:
                out += mapp[s[i]]
        return out + mapp[s[len(s)-1]] #The last digit is always added
    
    #FIRST ATTEMPT: FAIL because didnt group IV etc together but count them separately 
    def romanToInt(self, s: str) -> int:
        mapp = {'I': 1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        arr = [*s]
        out = 0
        for i,a in enumerate(arr):
            val = mapp[a]
            print(f"a={a}, prev={arr[i-1]}")
            if i != 0:
                if arr[i-1] == 'I':
                    print("if")
                    if a == 'V':
                        val = 4
                    if a == 'X': 
                        val = 9
                elif arr[i-1] == 'X':
                    print("else1")
                    if a == 'L':
                        val = 40
                    if a == 'C': 
                        val = 90
                elif arr[i-1] == 'C':
                    print("else2")
                    if a == 'D':
                        val = 400
                    if a == 'M': 
                        val = 900
            print(f"out{out} + val {val}")
            out += val
            print(f"out{out}")
        return out

#LESSON 1: The last digit is always added in roman numeral