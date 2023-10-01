#https://leetcode.com/problems/reverse-words-in-a-string-iii/?envType=daily-question&envId=2023-10-01
class Solution:
    def reverseWords(self, s: str) -> str:
        li = s.split(' ')
        re = []
        for word in li:
            word = word[::-1]
            print(f"word={word}")
            re.append(word)
        ans = ' '.join(re)
        return ans