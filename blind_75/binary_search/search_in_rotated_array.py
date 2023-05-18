class Solution:
    def search(self, nums: List[int], target: int) -> int:


        if target in nums:
            return nums.index(target)
        return -1
    
    
# Slightly faster

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        for x in nums:
            if x == target:
                return nums.index(target)
        return -1

    