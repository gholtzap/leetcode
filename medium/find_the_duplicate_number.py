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

# Solution 2
# O(n log(n)) | O(1)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
 
        nums.sort()

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]

          
# Solution 3
# O(n^2) | O(n)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for x in range(len(nums)):
            if nums[x] in nums[x+1:]:
                return nums[x]