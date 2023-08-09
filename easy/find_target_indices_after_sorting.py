# Solution 1
# O(n log(n)) | O(1)

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        nums.sort()

        return [i for i in range(len(nums)) if nums[i] == target]