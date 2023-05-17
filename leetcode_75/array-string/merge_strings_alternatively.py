# Solution 1 O(n) | O(n)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        output = ""
        lowerLimit = min(len(word1),len(word2))
        upperLimit = max(len(word1),len(word2))

        for x in range(0,lowerLimit):
            output+=word1[x]+word2[x]
           # output+=word2[x]
        
        if len(word1) == len(word2):
            return output

        if len(word1) > len(word2):
            tail = word1[lowerLimit:upperLimit]
        else:
            tail = word2[lowerLimit:upperLimit]
       
        return output+tail