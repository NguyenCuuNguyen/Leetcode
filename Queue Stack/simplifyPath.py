class Solution:
    def simplifyPath(self, path: str) -> str:
#         path = path[::-1] #.reverse()
#         res = [list(path)]
#         count = 0 #should be 0 (root) or >, -1 going up
#         for each in path:
#             if res[0] == "/":
                
#             elif count <= 0 and each == "/": #res[len(res)]
#                 res.pop()
        
#         return "".join(res)
        s = path.strip().split("/") #create a list of just dots and dirs
        res = []
        for each in s:
            if each == "..":
                if res: #not empty
                    res.pop()
                continue #keep going if it's empty
            elif each == "." or each == "/" or each == "":
                continue
            res.append(each)
        ans = ""
        for i in res:
            ans += "/"+i
        return "/" if not ans else ans 
