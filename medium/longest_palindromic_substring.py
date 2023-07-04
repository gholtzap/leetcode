# Solution 1
# O(n^2) | O(n)

class Solution:

    def isPalindrome(self, s:str) -> bool:
        return s[::-1] == s

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        l,r,output = 0,0,""

        while l < len(s):
            r = 0
           
            while r < len(s):
                if len(output) > r-l:
                    r+=1
                    continue
                temp = s[l:r+1]
                if self.isPalindrome(temp) and len(temp) > len(output):
                    output = temp
                r+=1
            l+=1
        return output

    


