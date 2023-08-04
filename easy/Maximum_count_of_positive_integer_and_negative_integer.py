# Solution 1
# O(n) | O(1)

class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        pos,neg = 0,0

        for x in nums:
            if x == 0:
                continue
            elif x <= 0:
                neg+=1
                continue
            pos+=1

        return max(pos,neg)
    
# Solution 2
# O(n) | O(n)


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
       return max(len([x for x in nums if x > 0]), len([x for x in nums if x < 0]))



