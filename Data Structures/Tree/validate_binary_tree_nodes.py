class Solution:
    #First attempt: fail to find root node, default to 0 but failed at other roots cases
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        #Index = root node numberID, array's element= child node numberID
        #Detect cylic tree
        #Valid binary tree: 
        #1. Only 1 root node without parent
            #Exactly n-1 unique values in both list
                #if lens(set(dic.keys())) >= n, return False
        #2. Each node, except root has at most 1 parent node
            # Create a dictionary, key=nodeID, value=parent's nodeID
                #If key already in dic, return False
        #3. All nodes are connected to root by association
            #write a helpr func to recursively look up until see root

        dic = {}
        def searchDictionary(dic, key):
            if key in dic:
                v = dic[key]
                if v == 0:
                    return v
                else:
                    return searchDictionary(dic, v)
            else:
                return None

        for i,node in enumerate(leftChild):
            if node != -1:
                if node not in dic:
                    dic[node] = i
                else:
                    return False
        for i,node in enumerate(rightChild):
            if node != -1:
                if node not in dic:
                    dic[node] = i
                else:
                    return False
        print(f"dic={dic}")
        if len(set(dic.keys())) >= n:
            return False
        for k,v in dic.items():
            if v != 0:
                root = searchDictionary(dic, v)
                if root != 0:
                    return False
        return True
                

#SOLUTION 1: Time O(N), Space O(N), not super efficient or modular
from queue import Queue
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        childCount = [False for x in range(n)] #length = n
        root = -1
        for i,left in enumerate(leftChild):
            if left != -1:
                childCount[left] = True
        for i,right in enumerate(rightChild):
            if right != -1:
                if childCount[right] == True:
                    return False
                childCount[right] = True
        print(f"childCount={childCount}")
        for node in childCount:
            if node == False:
                if root == -1:
                    root = childCount.index(node)
                else:
                    return False #multiple root
        if root == -1:
            return False #No root, invalid Binary tree
        #Breadth first search to validate:
        visited = [False] * len(leftChild)
        queue = Queue()
        queue.put(root)
        visited[root] = True
        while not queue.empty():
            cur = queue.get()
            if leftChild[cur] != -1:
                if visited[leftChild[cur]]:
                    return False #cyclic tree
                queue.put(leftChild[cur])
                visited[leftChild[cur]] = True
            if rightChild[cur] != -1:
                if visited[rightChild[cur]]:
                    return False #cyclic tree
                queue.put(rightChild[cur])
                visited[rightChild[cur]] = True
        print(f"visited={visited}")
        for visit in visited:
            if not visit:
                return False #Multiple components
        return True

#SOLUTION2: Depth first search, recursive and much more efficient:


from queue import Queue
class Solution:
    def DFS(self, cur:int, leftChild: List[int], rightChild: List[int], visited: List[int]) -> bool:
        if leftChild[cur] != -1:
            if visited[leftChild[cur]]:
                return False #cyclic tree
            visited[leftChild[cur]] = True
            if not self.DFS(leftChild[cur], leftChild, rightChild, visited):
                return False
        if rightChild[cur] != -1:
            if visited[rightChild[cur]]:
                return False #cyclic tree
            visited[rightChild[cur]] = True
            if not self.DFS(rightChild[cur], leftChild, rightChild, visited):
                return False
        
        return True

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        childCount = [False for x in range(n)] #length = n
        root = -1
        for i,left in enumerate(leftChild):
            if left != -1:
                childCount[left] = True
        for i,right in enumerate(rightChild):
            if right != -1:
                if childCount[right] == True:
                    return False
                childCount[right] = True
        print(f"childCount={childCount}")
        for node in childCount:
            if node == False:
                if root == -1:
                    root = childCount.index(node)
                else:
                    return False #multiple root
        if root == -1:
            return False #No root, invalid Binary tree

        visited = [False] * len(leftChild)
        visited[root] = True
        if not self.DFS(root, leftChild, rightChild, visited):
            return False

        for visit in visited:
            if not visit:
                return False #Multiple components
        return True
        

       


        


                


        
        
        


                


        
        
        
        
        