# Solution 1
# O(m+n) | O(1)

class Solution(object):
    def countNegatives(self, grid):
        i,j,count = len(grid)-1,0,0

        while i>=0 and j< len(grid[0]):
            if grid[i][j] < 0:
                count +=len(grid[0])-j
                i -= 1
            else:
                j +=1
        return count


# Solution 2
# O(n^2) | O(1)

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        output = 0

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] < 0:
                    output += len(grid[x]) - y
                    break


        return output