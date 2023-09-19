class Solution:
    """ (^з^)-♡   ٩(ˊᗜˋ*)و
    Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.
   
   Ex: Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
        Output: true
    """

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Optimised linear search:
        traversing the last column linearly till we reach the upper bound and then we traverse that row linearly(in reverse) until we find the number or the lower bound. """
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


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """Advanced binary search: start comparing from middle cell, if larger: move tail pass mid, go to the left. If smaller: move head pass mid, go to the right"""
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        
        while low <= high:
            mid = (low + high) // 2
        
            num = matrix[mid // cols][mid % cols]
            print(f"{mid=}, row={mid // cols}, column{mid % cols}: {num=}")
            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False
    
    
    """
    Correct:
    num = matrix[mid // cols][mid % cols]
    Output:        mid=5, row=1, column1: num=11
                    mid=2, row=0, column2: num=5
                    mid=0, row=0, column0: num=1
                    mid=1, row=0, column1: num=3
    
    Wrong:
    num = matrix[mid // cols][mid // cols]
    Output:     mid=5, row=1, column1: num=11
                mid=2, row=0, column2: num=1
                mid=3, row=0, column3: num=1
                mid=4, row=1, column0: num=11
    
    """