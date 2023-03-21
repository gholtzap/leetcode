class Solution {
    public int diagonalSum(int[][] mat) {

        int output = 0, y = 0;

        // iterate across the matrix, adding each diagonal # to output
        for(int i = 0; i<mat.length; i++){
            output+=mat[i][y] + mat[i][mat.length-i-1];
            y++;
        }

        // if matrix length is even, subtract the middle value
        if(mat.length%2 == 1){
            output -= mat[mat.length/2][mat.length/2];
        }

        return output;
    }

}