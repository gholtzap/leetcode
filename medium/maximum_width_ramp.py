# Solution 1
# O(n^2) | O(n)

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:

        output,l = 0,0

        for i in range(len(nums)-1,0,-1):
            for j in range(l,i):
                if nums[j] <= nums[i]:
                    output = max(i-j,output)

        return output