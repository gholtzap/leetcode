# Solution 1 
# O(n^2) | O(n)

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        prefixSum = [0] * (n+1)
        ans = 0
     
        for i in range(n):
            prefixSum[i+1] += prefixSum[i] + arr[i]

        for i in range(n):
            for j in range(i+1, n+1):
                if (j-i) % 2 == 1:
                    ans += prefixSum[j] - prefixSum[i]

        return ans

