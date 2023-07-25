# Solution 1
# O(n^2) | O(n)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        output = []

        for i in range(0,len(nums)-2):
            l,r = i+1,len(nums)-1
            
            target = 0-nums[i]
            
            while l < r:
                twosum = nums[l] + nums[r]
                temp = [nums[i],nums[l],nums[r]]
                if twosum == target and temp not in output:
                    output.append(temp)
                elif twosum > target:
                    r-=1
                else:
                    l+=1

        return output
        

        
        
        
           
        