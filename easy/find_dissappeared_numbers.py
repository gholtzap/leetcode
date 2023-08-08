# Solution 1
# O(n) | O(n)

from collections import Counter

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        lst = list(range(1,len(nums)+1))
        nums = list(set(nums))

        a = Counter(nums)
        b = Counter(lst)
        c = b - a

        return list(c.elements())
    
    