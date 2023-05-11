# Easiest solution: (kinda cheating)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()
        return nums[0]


# To do this prblem authentically, basically we need to replace nums.sort() with the most efficient sorting algorithm.
