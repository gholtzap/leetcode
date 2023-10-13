# Solution 1
# O(n) | O(1)

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        hashmap = {}

        for x in s:
            if x not in hashmap:
                hashmap[x] = 1
            else:
                hashmap[x] += 1

        for x in t:
            if x not in hashmap:
                return x
            if hashmap[x] == 0:
                return x
            else:
                hashmap[x] -=1

        return ""
        