class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        fixedString = ""

        for x in s:
            if x.isalnum():
                fixedString+=x
            
        if len(fixedString) == 0 or len(fixedString) == 1:
            return True

        left, right = 0,len(fixedString)-1

        while(left < right):
            if fixedString[left].lower() != fixedString[right].lower():
                return False
            left+=1
            right-=1
           
        return True