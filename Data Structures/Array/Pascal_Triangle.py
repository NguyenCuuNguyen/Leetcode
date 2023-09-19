"""Given an integer numRows, return the first numRows of Pascal's triangle.

"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        matrix = [[1], [1, 1]]
        if numRows == 0:
            return []
        elif numRows == 1:
            return [matrix[0]]
        elif numRows == 2:
            return matrix
        
        row = []
        for i in range(2, numRows): #i=2, j=(0,1)
            for j in range(i-1):
                row.append(sum(matrix[-1][j:j+2])) #start from last_row=matrix[-1], stop before column+2
            matrix.append([1] + row + [1])
            row = []
        return matrix



    """Any row can be constructed using the offset sum of the previous row.
            1 3 3 1 0 
        +   0 1 3 3 1
        =   1 4 6 4 1
    """
    def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            res += [list(map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1]))]
        return res[:numRows]
    