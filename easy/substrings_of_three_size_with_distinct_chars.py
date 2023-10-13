# Solution 1
# O(n^3) | O(n)

class Solution:
    def countGoodSubstrings(self, s: str) -> int:

        output = 0

        if len(s) < 3:
            return 0

        for i in range(len(s)-2):
            temp = []
            for j in range(i,i+3):
                if s[j] in temp:
                    break   
                temp.append(s[j])
            if len(temp) == 3:
                output+=1

        return output
        