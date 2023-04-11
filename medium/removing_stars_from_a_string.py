class Solution:
    def removeStars(self, s: str) -> str:
        stk = []
        i,n = 0,len(s)
   
        while i < n :
            if s[i] != '*':
                stk.append(s[i])
            else:
                stk.pop()
            i += 1
        return ''.join(stk)