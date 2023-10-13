# Solution 1
# O(n log(n)) | O(n)
    
    
class Solution:
    def sortSentence(self, s: str) -> str:
        
        arr = [] 
        # O(n)
        s = s.split(" ")
        
        # O(n)
        for x in s:
            arr.append([x[-1],x[0:len(x)-1]])

        # O(n log n)
        arr.sort()

        output = ""
        # O(n)
        for i in range(len(arr)-1):
            output += arr[i][1] + " "
        output += arr[-1][1]
        
        return output     