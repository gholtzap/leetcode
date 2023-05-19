# Solution 1
# O(n) | O(1)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        l,r = 0,1

        while r < len(nums):
            if nums[l] is 0 and nums[r] is not 0:
                nums[l] = nums[r]
                nums[r] = 0
                continue
            if nums[l] is 0 and nums[r] is 0:
                r+=1
                continue
  
            r+=1
            l+=1
            



