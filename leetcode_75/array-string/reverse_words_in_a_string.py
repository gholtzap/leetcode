# Optimal Solution
# O(n) | O(n)

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])

# Solution 2
# O(n) | O(n)

class Solution:
    def reverseWords(self, s: str) -> str:

        words = s.split()
        words = [word for word in words if word and word.strip()]
        
        return ' '.join(words[::-1])


# Solution 3
# O(n^2) | O(n)

class Solution:
    def reverseWords(self, s: str) -> str:

        x = s.split()
        x = [z for z in x if z and z.strip()]

        output = x[len(x)-1]
        
        for y in range(len(x)-2,-1,-1):
            output+=" "+x[y]
        
        return output
    
