# Solution 1

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numsSet = set(nums)
        output, count = 0,0

        for x in numsSet:
            pivot = x
            while pivot in numsSet:
                count+=1
                pivot+=1
           
            if count > output:
                output = count
            count = 0
            
        return output