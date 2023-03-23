import math

class Solution:
    # through trial and error, I have found that the no. of bulbs is equal to the
    # floored sqrt of n:int
    def bulbSwitch(self, n: int) -> int:
         return int(math.sqrt(n))
        