# Solution 1
# O(n) | O(1)


class Solution:
    def minOperations(self, nums: List[int]) -> int:

        output = 0

        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                temp = (nums[i] - nums[i+1]) +1
                output+= temp
                nums[i+1]+= temp

        return output
