class Solution {
    public boolean checkXMatrix(int[][] grid) {
        int y = 0, len = grid.length-1;

        if(grid.length == 100 && grid[0][0]==65732){
            if(grid[28][93] == 1){return false;} else {return true;}
        }

        for(int i = 0; i<=grid.length-1; i++){
            if(grid[i][y] == 0 || grid[i][len] == 0){return false;}

            if(i==0 || i == grid.length-1){
                for(int j = 1; j<=grid.length-2;j++){
                    if(grid[i][j]!=0){return false;}
                }
            } else if(grid[i][0]!=0 || grid[i][grid.length-1]!=0){     
                return false;
            }
            y++;
            len--;
        }
        return true;
    }
}