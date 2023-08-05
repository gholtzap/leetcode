# Solution 1
# O(n) | O(n)

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return len([x for x in hours if x >= target])