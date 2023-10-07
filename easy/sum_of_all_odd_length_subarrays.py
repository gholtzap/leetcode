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

# Solution 2
# O(n^3) | O(n)

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sums = []
        curr,j = -1,0
        # O(n)
        for i in range(len(arr)):
            j,temp=0,0
            curr+=2
            if curr > len(arr): break
            if j + curr > len(arr): continue

            # O(1) -> O(n)
            while j + curr <= len(arr):
                sums+=arr[j:j+curr]
                j+=1
        return sum(sums)


# Worst case O(n^3)