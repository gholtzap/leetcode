# First solution
# Time complexity: O(n), Space complexity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for i, x in enumerate(nums):
            if target - x in hashmap:
                return [i,hashmap[target-x]]
            hashmap[x] = i

            

# Second solution (brute force)
# Time complexity: O(n^2), space complexity: O(1)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in enumerate(nums):
            for y in range(i,len(nums)):
                if nums[i] + nums[y] == target and i is not y:
                    return [i,y]

