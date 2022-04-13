"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
=== Each row must contain the digits 1-9 without repetition.
=== Each column must contain the digits 1-9 without repetition.
=== Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
""""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """Every number can appear 9 times max. each number is unique per row&column and sub[i][j] (0->2) 81 cells in total, 
        How to iterate through different shape? Hashmap --> 3 hashmaps
        """
        row = {i:[] for i in range(9)}
        column = {i:[] for i in range(9)}
        box = {i:[] for i in range(9)}
        
        #First, iterate through matrix
        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                #to fix box number, find an algorithm calculating box_Num from any cell[i][j] within box  
                box_index = (i // 3) * 3 + (j //3)
                if cell == ".":
                    continue
                if cell in row[i] or cell in column[j] or cell in box[box_index]:
                    return False
                else:
                    row[i].append(cell)
                    column[j].append(cell)
                    box[box_index].append(cell)
        print(f"{row=}, {column=} and {box=}")
        return True


"""break the problem down:
Runtime: 95 ms, faster than 94.31% of Python3 online submissions for Valid Sudoku.
Memory Usage: 14 MB, less than 7.98% of Python3 online submissions for Valid Sudoku.
Time: O(N^2), Space: 

""""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (self.is_row_valid(board) and self.is_column_valid(board) and self.is_box_valid(board))
    
    def is_row_valid(self, board):
        for x in board:       #O(N) * O(N) = O(N^2)
            if not self.is_unit_valid(x):
                return False   
        return True
            
    def is_column_valid(self, board):
        transposed = zip(*board)
        for y in transposed: #O(N) * O(N) = O(N^2)
            if not self.is_unit_valid(y):
                return False
        return True
            
    def is_box_valid(self, board):
        for i in (0, 3, 6): # 3* 3* O(N) + O(N) = O(N)
           for j in (0, 3, 6): 
            #Tranpose the square into array
                array = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not self.is_unit_valid(array):
                    return False
        return True
            
    def is_unit_valid(self, unit):
        unit = [i for i in unit if i != '.'] #O(N)
        return len(set(unit)) == len(unit)