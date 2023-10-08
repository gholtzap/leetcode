# Solution 1
# O(n log(n)) | O(n)

class Solution:
    def addDigits(self, num: int) -> int:

        # O(log(n))
        while (num//10 != 0):
            temp = list(str(num))
            s = 0
            # O(n)
            for x in temp:
                s+= int(x)
            num = s

        return num
