# Solution 1
# O(n) | O(n)

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        if len(word) == 1:
            return True
        
        c,s = word[0],word[1:]

        return (c ==c.upper() and s == s.lower()) or (word == word.upper()) or (word == word.lower())