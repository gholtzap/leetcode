# Solution 1: O(N) O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:

        highest = 0
        left,right = 0,len(height)-1

        while left < right:
            area = (right-left) * min(height[left],height[right])
            highest = max(highest, area)

            if height[left] < height[right]:
                left+=1
            else:
                right-=1

        return highest


# Solution 2: O(n^2) O(1) 
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