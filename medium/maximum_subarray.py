class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # count:int stores the temp sum, which we will be comparing to 
        # record:int, which holds the highest sum (so far)
        
        count,record = 0,nums[0]


        for i in nums:
            # reset count when it falls below 0
            if count < 0:
                count = 0
            # add current index to count and compare it to our 'high score'.
            # winner takes record:int 's place.
            count += i
            record = max(count,record)
        return record
