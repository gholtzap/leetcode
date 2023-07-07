
# Solution 1
# O(n^2) | O(n)

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        answerKey = list(answerKey)
        output = 1

        for character in ['F', 'T']:
            for i in range(len(answerKey)):
                temp, score = k, 0
                for j in range(i, len(answerKey)):
                    if temp < 1 and answerKey[j] == character:
                        break
                    score += 1
                    if answerKey[j] == character:
                        temp -= 1
                output = max(output, score)

        return output