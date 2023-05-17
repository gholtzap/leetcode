# Solution 1 O(n) | O(1)

class Solution:
    def canPlaceFlowers(self, flowers: List[int], n: int) -> bool:

        # Base cases
        if len(flowers) == 1 and flowers[0] == 0:
            return True
        if len(flowers) == 0:
            return False
        if 0 not in flowers and n>0:
            return False

        lenFlowers = len(flowers)

        # Checking edges of array (beginning index and last index)
        if flowers[0] == 0 and flowers[1] == 0 and n>0:
            flowers[0] = 1
            n-=1
        if flowers[lenFlowers-1] == 0 and flowers[lenFlowers-2] == 0 and n>0:
            flowers[lenFlowers-1] = 1
            n-=1

        # Standard algorithm
        for x in range(1,len(flowers)-1):
            if flowers[x] == 0 and flowers[x-1] == 0 and flowers[x+1] == 0 and n>0:
                flowers[x] = 1
                n-=1
        
        return n == 0
            

