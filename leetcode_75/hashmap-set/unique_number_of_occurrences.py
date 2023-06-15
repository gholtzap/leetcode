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
    
# Solution 2
# O(n) | O(n)

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        dt = {}
        temp = []

        for x in arr:
            if x in dt:
                dt[x]+=1
            else:
                dt[x]=1

        for x in dt:
            if dt[x] in temp:
                return False
            temp.append(dt[x])

        return True
