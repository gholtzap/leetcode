# Solution 1
# O(n) | O(n)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
 
        hashmap = {}

        for i in range(len(nums)):
            if nums[i] in hashmap:
                return nums[i]
            hashmap[nums[i]] = 0
        return 0

