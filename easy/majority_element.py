class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # sort array, then find middle element
        # floor divison is necesary due to int conversion for calling nums[x]
        nums.sort()
        return nums[len(nums)//2]