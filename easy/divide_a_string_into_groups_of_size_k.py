# Solution 1
# O(n) | O(n)

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:

        output = []

        for i in range(0,len(s),k):
            output.append(s[i:i+k])

        for i in range(len(output)):
            while len(output[i]) < k:
                output[i] += fill

        return output
        