#Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of S.


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        #removing outer parentheses of each decomposed part:
        balance = 0
        i = 0
        result = []
        for j in range(len(s)): #j goes from 0 to s-1
            if s[j] == "(": #go here first, rather than if balance == 0 
                balance += 1
            elif s[j] == ")":
                balance -= 1
            if balance == 0:
                result.append(s[i+1:j])
                i=j+1
        return "".join(result)
            
