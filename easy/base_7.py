# Solution 1
# O(log7 n) | O(1)

class Solution:
    def convertToBase7(self, num: int) -> str:
        
        output = ""
        if num < 0:
            output+="-"
        num = abs(num)
        
        count,temp = 0,num
        while temp >= 7:
            temp//=7
            count+=1


        for i in range(count,-1,-1):
            count = 0
            while num >= pow(7,i):
                num -= pow(7,i)
                count+=1
            output += str(count)
        return output