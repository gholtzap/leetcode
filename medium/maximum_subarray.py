class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        count,record = 0,nums[0]

        for i in nums:
            if count < 0:
                count = 0
            count += i
            record = max(count,record)
        return record
