# My first Approach
# Time complexity: O(n), Space complexity: O(n)
# Create dict with key:value, where key is a character and value is the amount of times it appears in the string
# Iterate through T and subtract 1 from each value if key is in T | If key < = 0, return False | If key is not in dict, return False


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        dc = {}

        for x in s:
            if x not in dc:
                dc[x] = 1
            else:
                dc[x] +=1

        for y in t:
            if y in dc:
                if dc[y] > 0:
                    dc[y]-=1
                    
            else:
                return False

        for z in dc.values():
            if z > 0:
                return False

        return True
    
    
# Second attempt
# Time complexity: O(nlogn) Space complexity: O(n)
# Convert each string to a list, then sort. Then return if it's equal

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
 
        sList = list(s)
        sList.sort()
        
        tList = list(t)
        tList.sort()

        return tList == sList