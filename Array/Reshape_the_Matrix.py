class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        """mat = [[1,2],[3,4]], r = 1, c = 4
           m-rows x n-columns
           r*c =sum(len(x)) for x in mat
        Time: O(r*c), Space: O(N)
           """
        #r = num of sub-arrays, c = num of elements   
        exploded = []
        matrix = []
        for m in mat:
            exploded.extend(m)           
        print(f"{exploded=}")
        if r*c != len(exploded):
            return mat
        else:
            for i in range(0, len(exploded), c):
                matrix.append(exploded[i:i+c])
        return matrix