# Solution 1 (optimal runtime):
#   Create Hashmap. Iterate through array. If item in hashmap, return True, else add value to hashmap.
#   O(n) runtime, O(n) space

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        if len(nums) == 0 or len(nums) == 1 :
            return False

        hashmap = {}

        for x in nums:
            if x in hashmap:
                return True
            hashmap[x] = 0

        return False
    
    
# Solution 2 (optimal space):
#   Sort array, then iterate through and check if the next number is equal
#   O(log(n)), space O(1)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        nums.sort()

        if len(nums) == 0 or len(nums) == 1 :
            return False

        for x in range(len(nums)-1):
            if nums[x]==nums[x+1]:
                return True

        return False
    
    
# Solution 3 (bonus):
#   Convert to HashSet, if len(HashSet) == len(List) return False  else return True

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        if len(nums) == 0 or len(nums) == 1 :
            return False

        hashset = set(nums)

        return not len(hashset) == len(nums)