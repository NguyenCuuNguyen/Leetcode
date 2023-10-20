#https://leetcode.com/problems/parallel-courses-iii/description/?envType=daily-question&envId=2023-10-18
class Solution:
    #Failed first attempt: only work for base case, could't figure out recursive solution
    #I figured the calculation of max time among preqs has to be recursive
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        #brute force
        ans = 0
        minNext = n #min of relations[j][1], anything from range(1,nextCourse) is taken simul
        for i,pair in enumerate(relations):
            minNext = min(relations[i][1], minNext)
        maxTime = max(time[0:minNext-1]) #from previous preq to minReq
        print(f"minNext={minNext}, maxTime={maxTime}")
        ans += maxTime + time[minNext-1]
        #next is not last element
        if minNext != n:
            ans += self.minimumTime
        return ans

#SOLUTION 1: MEMOIZATION & DEPTH FIRST SEARCH
class Solution:
    ## n = 5, relations = [[1,5],[2,5],[3,5],[3,4],[4,5]], time = [1,2,3,4,5]
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        #Create a graph to represent the prerequisites using an adjacency list.
        graph = [[] for _ in range(n)]
        for prev, nex in relations:
            graph[prev-1].append(nex-1) #[[4], [4], [4, 3], [4], []]
        #Create a memoization table (an array) to store the minimum time needed to complete each course.
        memoi = [-1] *n
        print(f"graph={graph}")
        #Define a recursive function to calculate the minimum time to complete a course:
        def calcMinTime(course):#:int, graph:List[List[int]], memoi: List[int]):
            # a. If the course has already been calculated, return its value from the memoization table.
            if memoi[course] != -1:
                return memoi[course]
            # b. If the course has no prerequisites, its time is simply its own duration.
            if not graph[course]: #all O-based indexing 
                memoi[course] = time[course]
                return memoi[course]
            # c. Otherwise, calculate the time to complete this course as the maximum time among its prerequisites plus its own duration.
            maxPreqTime = 0
            for preq in graph[course]:
                maxPreqTime = max(maxPreqTime, calcMinTime(preq))
            memoi[course] = maxPreqTime + time[course]
            # d. Store this calculated time in the memoization table and return it.
            return memoi[course]
        # Initialize a variable to keep track of the overall minimum time.
        globalMin = 0
        # For each course, calculate its minimum time using the recursive function and update the overall minimum time if necessary.
        for course in range(n):
            globalMin = max(globalMin, calcMinTime(course))
        # The overall minimum time is the answer.
        print(f"memoi={memoi}")
        return globalMin
#LESSON 1: can traverse 2D array by say for prev, next in 2DARRAY: