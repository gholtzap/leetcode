# Solution 1    
# O(n^2) | O(n)
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return goal in s + s and len(goal) == len(s)