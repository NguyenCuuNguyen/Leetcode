#https://leetcode.com/problems/flatten-nested-list-iterator/description/?envType=daily-question&envId=2023-10-20
#Failed first attempt, didn't think of recursion because didn't accoutn for all cases:
#LESSON: calm down, don't worry about getting the coding right, focus on the general problem, identify patterns and logic first.
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
#SOLTION 1: Flattening the list and use that instead
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = nestedList
        self.flat = []
        self.cur = 0
        def recursion(nest):
            for n in nest:
                if n.isInteger():
                    self.flat.append(n.getInteger())
                else:
                   recursion(n.getList())
        recursion(self.nestedList)
    def next(self) -> int:
        self.cur += 1
        return self.flat[self.cur-1]
            
    def hasNext(self) -> bool:
        return self.cur < len(self.flat)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

#
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """

#SOLUTION 2: Use stack:
#hasNext() ensures top of stack always has int, if  not, pop list out and put back in reverse as int. 
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]
    def next(self) -> int:
        return self.stack.pop()
            
    def hasNext(self) -> bool:
        while self.stack:
            cur = self.stack[-1] #top of stack, nestedList[0]. Don't pop it because we want to preserve the order of remaining item for concat later.
            print(f"cur={cur}, type={type(cur)}")
            if cur.isInteger():
                return True
            self.stack = self.stack[:-1] + cur.getList()[::-1]#remaining stack + reversed nested list to pop in right order later. Keep looping and popping int top of stack, if not then fix and pop int top. Use getList() because all elements are 'precompiled.nestedinteger.NestedInteger' type
        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = nestedList
        self.curi = 0
        self.curj = 0
        # leni = len(nestedList)

    def next(self) -> int:
        for i in self.nestedList[self.curi:]:
            for j in self.nestedList[self.curi][j]:
                self.curi += 1
                if type(self.nestedList[self.curi]) != int:
                    self.curj = j+1
                    return self.nestedList[self.curi-1][self.curj-1]
                else:
                    return self.nestedList[self.curi-1]
            
    def hasNext(self) -> bool:
        if self.nestedList[self.curi] != self.nestedList[-1]:
            return True
        else:
            if type(self.nestedList[self.curi]) != int:
                if self.nestedList[self.curi][self.curj]:
                    return True
                else:
                    return False
        return False