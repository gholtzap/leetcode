# Solution 1 
# O(n^2) | O(n)

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        temp = []
        s = set(arr)

        for x in s:
            tempCount = arr.count(x)
            if tempCount in temp:
                return False
            temp.append(arr.count(x))
        return True
    
