# Solution 1
# O(n^2) | O(n)


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows,columns = [],[]

        for i in range(len(matrix)):
            for j in range(len(matrix[i])): 
                if matrix[i][j] == 0:
                    rows.append(i)
                    columns.append(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in rows or j in columns:
                    matrix[i][j] = 0
