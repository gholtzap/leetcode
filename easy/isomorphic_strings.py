# Solution 1
# O(n) | O(n)


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        hashmap = {}

        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = t[i]
            else:
                if t[i] != hashmap[s[i]]:
                    return False
            
        if len(set(hashmap.values())) != len(hashmap.values()):
            return False

        return True