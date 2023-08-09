# Solution 1
# O(n) | O(n)

class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        digits,product, sm = list(str(n)),1,0

        for x in digits:
            product *=int(x)
            sm+=int(x)
        
        return product - sm