# Solution 1
# O(n), O(n)

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        if k == 0:
            return nums
        if len(nums) <= k+k:
            return [-1 for _ in range(len(nums))]
        
        output = [-1 for _ in range(k)]
        
        tempSum = sum(nums[0:k*2+1])
        output.append(tempSum//((k*2)+1))

        for i in range(k,len(nums)-k-1):
            tempSum += nums[i+k+1]
            tempSum -= nums[i-k]
            output.append(tempSum//((k*2)+1))

        return output + [-1 for _ in range(k)]