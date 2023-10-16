#https://leetcode.com/problems/pascals-triangle-ii/?envType=daily-question&envId=2023-10-16
class Solution:
    #SOLUTION 1: first attempt, Time O(N^2), space O(2*N) = O(N), not optimal
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1,1]
        if rowIndex == 0:
            return row[0:1]
        elif rowIndex == 1:
            return row
        else:
            new_row = row.copy()
            for it in range(2, rowIndex+1):
                i = 1
                print(f"row={new_row}, iter={it}")
                while i < it:
                    new_row[i] = row[i-1] + row[i]
                    print(f"row index{i}={row[i-1]} + {row[i]}")
                    i+=1
                new_row.append(1)
                row = new_row.copy()
                print(f"new_row={new_row}")
        return row
    
#SOLUTION 2: using Pascal triangle's binomial theorem's consecutive number's property to generate array directly without prev rows
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        prev = 1
        for k in range(1, rowIndex+1):
            nex = prev * (rowIndex - k +1) // k
            row.append(nex)
            prev = nex
        return row

#SOLUTION 3: Worse than solution 1, Space O(N^2) because storing whole triangle
# Initialize 2D Vector: Create a 2D vector pascalTriangle with numRows rows to represent Pascal's Triangle.
# Generate Rows: Generate first row seperately then Loop through each row from 1 to numRows (inclusive).
# Set First and Last Elements: Set the first and last elements of each row to 1.
# Calculate Middle Elements: For each row, calculate and append the middle elements by adding the corresponding elements from the previous row.
# Return Last computed row.
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr = [[1], [1,1]] #num inner arrays = rowIndex
        if rowIndex in (0,1):
            return arr[rowIndex]
        for r in range(2,rowIndex+1):
            row = [1]
            #calculate middle elements:
            for i in range(1,r):
                print(f"in row {r}={row}, i={i}")
                nex = arr[r-1][i-1] + arr[r-1][i]
                row.append(nex)
                print(f"row={row}")
            row.append(1)
            arr.append(row)
            print(f"arr={arr}")
        return arr[-1]




        