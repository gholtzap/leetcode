# Solution 1
# O(n^2) | O(n)

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        lst = list()

        # nested for-loop: O(n^2)
        for x in matrix:
            for y in x:
                lst.append(y)

        # .sort() : O(n log(n))
        lst.sort()
        return lst[k-1]