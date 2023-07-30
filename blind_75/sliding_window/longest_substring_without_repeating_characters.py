# Solution 1
# O(n^3) | O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0 or len(s) == 1:
            return len(s)

        l,r,output = 0,0,1
        
        while r < len(s):
            r+=1
            temp = s[l:r]
            if not len(temp) == len(set(temp)):
                l+=1
                continue
            output = max(len(temp),output)  

        return output


# Solution 2
# O(n) | O(n)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charSet = set()
        l,highScore = 0,0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            highScore = max(highScore,r-l+1)  
        return highScore