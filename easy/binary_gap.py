# Solution 1
# O(n^2) | O(n)

class Solution:
    def binaryGap(self, n: int) -> int:

        n = list(bin(n)[2:])

        if n.count('1') == 1 or n.count('1') == 0:
            return 0

        output = 0
        for i in range(len(n)):
            temp = 0
            if n[i] == '1':
                for x in range(i+1,len(n)):
                    if n[x] == '1':
                        temp+=1
                        output = max(output,temp)
                        break
                    else:
                        temp+=1                    
        return output