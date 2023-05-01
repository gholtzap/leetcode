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