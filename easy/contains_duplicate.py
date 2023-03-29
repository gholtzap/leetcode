class Solution(object):
    def containsDuplicate(self, nums):

        nums.sort()

        if len(nums)==1:
            return False
        
        for x in range(len(nums)-1):
            if nums[x] == nums[x+1]:
                return True
        
        return False