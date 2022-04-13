class Solution:
    """ (^з^)-♡
    Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.
   
   Ex: Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
        Output: true
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix) #3
        column = len(matrix[0]) #4
        
        for i in range(row):
            for j in (0, column-1):
                print(f"{matrix[i][j]=}")
                if matrix[i][j] == target:
                    return True
                elif matrix[i][j] > target:
                    for x in matrix[i]:
                        if x == target:
                            return True
                        
        return False