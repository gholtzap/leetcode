class Solution:
    def isValid(self, s: str) -> bool:
    
        if len(s) % 2 == 1:
            return False

        hashmap = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        stack = []
      
        for x in s:
            if x in hashmap:
                if len(stack) == 0:
                    return False
                if stack[-1] not in hashmap[x]:
                    return False
                stack.pop()
                
            else:
                stack.append(x)

        return len(stack) == 0