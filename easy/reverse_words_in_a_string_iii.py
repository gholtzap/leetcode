# Solution 1
# O(n) | O(n)


class Solution:
    def reverseWords(self, s: str) -> str:

        words = s.split(' ')
        output = ""
        for i in range(len(words)-1):
            output+= self.reverse(words[i]) + " "
                
        output+=self.reverse(words[-1])

        return output

    
    def reverse(self, s:str) -> str:
        return s[::-1]
    
    
# Solution 2 (Solution 1 logic except not optimized for readability)
# O(n) | O(n)

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(word[::-1] for word in s.split(' '))


    
