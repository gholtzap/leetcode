# Solution 1
# O(n) | O(n)

class Solution:
    def calPoints(self, operations: List[str]) -> int:

        q = []

        for x in operations:
            match(x):
                case 'D':
                    q.append(int(q[-1])*2)                
                case 'C':
                    q.pop()
                case '+':
                    q.append(int(q[-1]) + int(q[-2]))
                case _:
                    q.append(int(x))

        return sum(q)
    
    
# Solution 2
# O(n) | O(n)

class Solution:
    def calPoints(self, operations: List[str]) -> int:

        q,score = [],0

        for x in operations:
            match(x):
                case 'D':
                    val = q[-1]*2
                    q.append(val)
                    score += val                
                case 'C':
                    val = q.pop()
                    score -= val
                case '+':
                    val = q[-1] + q[-2]
                    q.append(val)
                    score += val
                case _:
                    val = int(x)
                    q.append(val)
                    score += val

        return score