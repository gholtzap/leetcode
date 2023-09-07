# Solution 1
# O(n + m) | O(n + m)

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        
        return [c[0] for c in words] == list(s)
