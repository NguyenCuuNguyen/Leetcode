#https://leetcode.com/problems/integer-to-roman/
class Solution:
    #SOLUTION 1: Divide range into groups of tens and use mod & division to look up values
    def intToRoman(self, num: int) -> str:
        M = ["", "M", "MM", "MMM"] #MAX == 3999
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num//1000] + C[num%1000//100] + X[num%1000%100//10] + I[num%1000%100%10]
    
    #SOLUTION 2: use map and search in list of value then decrement num:
    def intToRoman(self, num: int) -> str:
        re = ''
        mapp = {1:'I', 5:'V', 4: 'IV',
                9:'IX', 10:'X', 50:'L', 40:'XL',
                90: 'XC', 100:'C', 400:'CD', 500:'D',
                900:'CM', 1000:'M'}
        re = ''
        for n in reversed([1,4,5,9,10,40,50,90,100,400,500,900,1000]):
            while n <= num:
                re += mapp[n]
                num -= n
        return re
    

    #First attempt: fail
    def intToRoman(self, num: int) -> str:
        re = ''
        length = len(str(num))
        num = str(num)
        mapp = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        for n in range(length):
            length = length - 1
            tens = 10 ** length
            unit = int(num[n]) * tens
            print(f"num[n]={num[n]}, unit={unit}, subLength={length}")
            if unit in mapp:
                re += mapp[unit]
            else:
                if unit % 4 == 0:
                    #IV=4 XL=40 CD=400
                    if tens == 0:
                        re += 'IV'
                    elif tens == 10: 
                        re += 'XL'
                    elif tens == 100:
                        re += 'CD'
                elif unit % 9 == 0:
                    if tens == 0:
                        re += 'IX'
                    elif tens == 10: 
                        re += 'XC'
                    elif tens == 100:
                        re += 'CM'
                else:
                    if tens == 0:
                        tens = 1
                    form = mapp[tens]
                    re += int(num[n]) * form
                    
            print(f"re={re}")

        return re