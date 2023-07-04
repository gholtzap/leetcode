# Solution 1
# O(n^2) | O(n)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows,columns = [],[]
        l = len(matrix[0])
        
        for i in range(len(matrix)):
            for j in range(l): 
                if matrix[i][j] == 0:
                    rows.append(i)
                    columns.append(j)

        for i in range(len(matrix)):
            if i in rows:
                matrix[i] = [0] * l
                continue
            for j in range(l):
                if j in columns:
                    for k in range(0,len(matrix)):
                        matrix[k][j] = 0
                    continue
            

# Solution 2
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
