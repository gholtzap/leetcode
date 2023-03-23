class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # iterate through nums and check which number only returns 1 from count() function
        for i in range(len(nums)):
            if(nums.count(nums[i]) == 1):
                return nums[i]
        
        return 0