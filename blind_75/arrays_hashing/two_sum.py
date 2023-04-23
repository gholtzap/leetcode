# First solution
# Time complexity: O(n), Space complexity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for i,n in enumerate(nums):
            if target - n in hashmap:
                return [i,hashmap[target-n]]
            hashmap[n] = i


# Second solution (brute force)
# Time complexity: O(n^2), space complexity: O(1)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

 
        for i, n in enumerate(nums):
            for j, m in enumerate(nums):
             
                if m + n == target and i is not j:
                    return [i,j]

    