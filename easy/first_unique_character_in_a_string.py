# Solution 1
# O(n) | O(1)

class Solution:
    def firstUniqChar(self, s: str) -> int:

        for i in range(len(s)):
            if s.count(s[i]) < 2:
                return i

        return -1
    
    
# Solution 2
# O(n) | O(n)

class Solution:
    def firstUniqChar(self, s: str) -> int:

        visited,i = {}, 0
        
        while i < len(s):
            if s[i] in visited:
                i+=1
                continue
            if s.count(s[i]) < 2:
                return i
            visited[i] = 0
            i+=1
        return -1