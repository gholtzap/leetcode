# Solution 1
# O(n^2) | O(n)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(t) == 0 and len(s) == 0:
            return True
        if len(t) == 0 and len(s) > 0:
            return False
        if len(s) == 0:
            return True

        st = list(s)

        for i in range(len(st)):
            if st[i] in t:
                t = t[t.index(st[i])+1:]
            else:
                return False
                
        return True
