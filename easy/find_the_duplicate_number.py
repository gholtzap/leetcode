# Solution 1

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        nums.sort()

        for x in range(len(nums)):
            if nums[x] == nums[x+1]:
                return nums[x]

# Solution 2
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        hashmap = {}

        for x in nums:
            if x in hashmap:
                return x
            hashmap[x] = 0
            
# Solution 3
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for x in nums:
            if nums.count(x) > 1:
                return x
            
# Solution 4
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for x in range(len(nums)):
            if nums[x] in nums[x+1:]:
                return nums[x]
