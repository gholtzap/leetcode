# Solution 1
# O(n^2) | O(n^2)

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        subarrays = []
        for x in range(len(nums)):
            temp = [nums[x]]
            for y in range(x,len(nums)-1):
                if nums[y+1] > nums[y]:
                    temp.append(nums[y+1])
                else:
                    break
            subarrays.append(temp)
        
        output = 0
        for x in subarrays:
            sm = sum(x)
            output = max(output,sm)

        return output
        