#https://leetcode.com/problems/number-of-flowers-in-full-bloom/?envType=daily-question&envId=2023-10-11
from collections import defaultdict
class Solution:
    #SOLUTION 1:  space O(P), time O(P^2)
    #Intuition: At time t, # of blooming = # started blooming - # stopped blooming
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        ans = []
        dic = defaultdict(int)
        for start, end in flowers:
            dic[start] += 1
            dic[end+1] -= 1
        print(dic) #{1: 1, 7: -1, 3: 1, 8: -1, 9: 1, 13: -1, 4: 1, 14: -1}
        status, count = {}, 0
        #Reverse people's time to pop back in correct order
        remain_peo = sorted(people, reverse=True)
        #Iterate whenever there's an update in number of flower
        for time in sorted(dic.keys()):
            change = dic[time]
            print(f"time={time}, change={change}, remain_peo={remain_peo}")
            #While there're peo & flower num is updated after first per in queue visits 
            while remain_peo and time > remain_peo[-1]:
                status[remain_peo.pop()] = count
                print(f"status={status}")
            if not remain_peo:
                break
            #update count after assigning prev count to the person's visit
            count += change
            print(f"count is updated={count}\n")
        print(f"status={status}, people={people}")
        return [status[p] if p in status else 0 for p in people]
        

    #First attempt fail: Brute force Time=O(P*(F^2)), Space=O(P)
    #Intuition: Because People's array's length == answer's length, we iterate through people's length and keep count of the flowers at bloom during people's visit
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        ans = []
        for i,time in enumerate(people):
            count = 0
            for bloom in flowers:
                start = bloom[0] 
                end = bloom[1] + 1 #+1 for inclusive range
                
                count += 1 if time in range(start, end) else 0
                print(f"count={count}")
            ans.append(count)
        print(f"ans={ans}")
        return ans


    #Second attempt: fail because too slow
    #Intuition: Only iterate through flower's 2D array once to reduce runtime, sacrificing Space 
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        ans = []
        dic = {}
        for bloom in flowers:
            start = bloom[0] 
            end = bloom[1] + 1 #+1 for inclusive range
            for i in range(start,end):
                if i not in dic:
                    dic[i] = 1
                else:
                    dic[i] += 1
            print(f"dic={dic}, keys={sorted(dic.keys())}")
        
        for peo in people:
            if peo in dic:
                ans.append(dic[peo])
            else:
                ans.append(0)
        return ans
            


