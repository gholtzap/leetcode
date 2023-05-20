# Solution 1
# O(n^2)

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:


        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            if nums[0] + nums[1] is not k:
                return 0
        
        l,r,output = 0,1,0

        while r < len(nums) and l < len(nums)-1:
            if nums[l] + nums[r] == k:
                nums.pop(r)
                nums.pop(l) 
                output+=1
                l = 0
                r = 0
                
            elif r == len(nums)-1:
                l+=1
                r=l+1
                continue
            else:
                r+=1
                
        return output