# Solution 1
# O(n^3) | O(n)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        l, r = 0, 0
        output, output_len = "", 0

        while l < s_len:
            if s_len - l <= output_len:
                return output 
            r = 0
            while r < s_len:
                if output_len > r - l:
                    r += 1
                    continue
                if output_len < r - l + 1:
                    temp = s[l:r+1]
                    if temp[::-1] == temp:
                        output = temp
                        output_len = r - l + 1
                r += 1
            l += 1
        return output

    


