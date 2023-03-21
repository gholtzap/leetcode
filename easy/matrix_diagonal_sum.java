class Solution {
    public int diagonalSum(int[][] mat) {

        int output = 0, y = 0, len = mat.length-1, mid = mat.length/2;

        // iterate across the matrix, adding each diagonal # to output
        for(int i = 0; i<mat.length; i++){
            output+=mat[i][y] + mat[i][len];
            len--;
            y++;
        }

        // if matrix length is even, subtract the middle value
        if(mat.length%2 == 1){
            output -= mat[mid][mid];
        }

        return output;
    }

}