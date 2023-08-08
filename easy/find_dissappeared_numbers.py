# Solution 1

from collections import Counter

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        lst = list(range(1,len(nums)+1))
        nums = list(set(nums))

        a = Counter(nums)
        b = Counter(lst)
        c = b - a

        return list(c.elements())
    
    
# Solution 2

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        return [x for x in list(range(1,len(nums)+1)) if x not in nums]