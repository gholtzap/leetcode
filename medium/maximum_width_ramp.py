# Solution 1
# O(n log(n)) | O(n)

class Solution:
    def maxWidthRamp(self, nums:List[int]) -> int:
        stack, r = [], 0
        for i, a in enumerate(nums):
            if not stack or nums[stack[-1]] > a:
                stack.append(i)

        print(stack)
        
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                r = max(r, j - stack.pop())
        return r

# Solution 2
# O(n^2) | O(1)

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:

        output,l = 0,0

        for i in range(len(nums)-1,0,-1):
            for j in range(l,i):
                if nums[j] <= nums[i]:
                    output = max(i-j,output)

        return output