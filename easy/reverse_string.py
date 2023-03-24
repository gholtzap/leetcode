class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        l,r = 0,len(s)-1
        temp = ''

        # iterate through chars in s while left pointer hasnt crosses right pointer
        while(l < r):
            # swaps char at l:int with char at r:int
            temp = s[l]
            s[l]=s[r]
            s[r]=temp

            l+=1
            r-=1