# Solution 1
# O(n * m) | O(n)

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        output,temp = [],[]

        for i in range(1,n+1):
            if temp == target:
                return output
            output.append("Push")
            if i not in target:
                output.append("Pop")
            else:
                temp.append(i)
        return output