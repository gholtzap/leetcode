# Solution 1
# O(n^2) | O(n)

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1:
            return [[1]]

        output = [[1],[1,1]]

        if numRows == 2:
            return output
        
        currRow = 1
        numRows-=2
        
        while numRows > 0:
            currRow+=1
            temp = [1]
            for i in range(1,currRow):
                temp.append(output[currRow-1][i-1]+output[currRow-1][i])
            temp.append(1)
            output.append(temp)
            numRows -=1
    

        return output