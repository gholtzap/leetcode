# Solution 1
# O(n) | O(n)

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        output,arr,i = 0,list(columnTitle),len(arr)-1
        
        for x in arr:
            output += ((ord(x)-64)*(pow(26,i)))
            i-=1

        return output
