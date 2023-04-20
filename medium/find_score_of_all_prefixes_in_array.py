class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        ans, rm, rp = [], 0, 0
        for num in nums:
            rm = max(rm, num)
            rp += rm + num
            ans.append(rp)
        
        return ans