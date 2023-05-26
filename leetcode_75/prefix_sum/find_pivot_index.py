# Solution 1
# O(n) | O(1)

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        totalSum,leftSum = sum(nums),0

        for i,x in enumerate(nums):
            rightSum = totalSum - leftSum - x
            if rightSum == leftSum:
                return i
            leftSum += x
        return -1



# Solution 1
# O(n^2) | O(2n)

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        if len(nums) == 1:
            if nums[0] == 0:
                return 0
            return -1

        sumL, sumR = 0,0
        tempL,tempR = [],[]

        for i,x in enumerate(nums):
            tempL,tempR = [],[]
            for j in range(0,i):
                tempL.append(nums[j])
            for k in range(i+1,len(nums)):
                tempR.append(nums[k])
            sumL,sumR = sum(tempL),sum(tempR)
            if sumL == sumR:
                return i

        return -1

