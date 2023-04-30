# Solution 1: O(n^2) O(1) 
# Way too slow. Not practical

class Solution:
    def maxArea(self, height: List[int]) -> int:

        highest = 0
        n = len(height)

        for i in range(n-1):
            for j in range(i+1, n):
                area = (j-i) * (min(height[j],height[i]))
                highest = max(highest, area)
      
        return highest