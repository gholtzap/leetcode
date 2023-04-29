# Solution 1
# O(n), O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left,right = 0,len(numbers)-1

        while True:

            num = numbers[left] + numbers[right]

            if num == target:
                return [left+1,right+1]

            if num < target:
                left+=1
            elif num > target:
                right-=1

# Solution 2
# O(n^2),O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0

        while left<len(numbers):
            for x in range(left+1,len(numbers)):     
                if numbers[left] + numbers[x] == target:
                    return [left+1,x+1]

            left+=1