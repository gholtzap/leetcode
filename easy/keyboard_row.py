# Solution 1
# O(n * m ) | O(n * m)

class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        rows = [set("qwertyuiopQWERTYUIOP"), set("asdfghjklASDFGHJKL"), set("zxcvbnmZXCVBNM")]

        return [word for word in words if any(all(char in row for char in word) for row in rows)]
