class Solution {
    public int numIslands(char[][] grid) {
       //Queue<Integer> queue = new LinkedList<>();
        int count = 0;
        for(int i = 0; i < grid.length; i++){
            for(int j = 0 ; j< grid[i].length; j++){
                if(grid[i][j] == '1'){
                    BFSzero(grid, i, j); //zero out all connected 1 from newly found '1'
                    count += 1; //when see a 1, found at least 1 island
                }
            }
        }
        return count;
    }
    public void BFSzero(char[][] grid, int i, int j){
        //do boundary check
        if (i < 0 || i >= grid.length || j < 0 || j >= grid[i].length || grid[i][j] == '0')
            return;
        grid[i][j] = '0'; //if '1', set it right to 0, so won't see it again
        //recursive calls
        BFSzero(grid, i+1, j); //up
        BFSzero(grid, i-1, j); //down
        BFSzero(grid, i, j-1); //left
        BFSzero(grid, i, j+1); //right
    }
}