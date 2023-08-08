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
    

# Solution 3

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        output = []


        #print(f"NUMS {nums} LEN {len(nums)}")
        for i in range(1, len(nums)+1):
            #print(f"i {i} \t ")
            if i not in nums:
                output.append(i)

        return output