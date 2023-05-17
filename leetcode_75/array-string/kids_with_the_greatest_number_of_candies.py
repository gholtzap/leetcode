# Optimal
# O(n) | O(1)

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        bar = max(candies)-extraCandies
        return [candy>=bar for candy in candies]


# Solution 1
# O(n) | O(n)

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        output = []
        highestCandies = max(candies)

        for x in candies:
            if x + extraCandies >= highestCandies:
                output.append(True)
            else:
                output.append(False)

        return output
    
    
# Solution 2
# O(n) | O(n)

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        output = []
        bar = max(candies)-extraCandies

        for x in candies:
            if x >= bar:
                output.append(True)
            else:
                output.append(False)

        return output
    
