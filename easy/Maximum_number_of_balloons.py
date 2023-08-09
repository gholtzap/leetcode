# Solution 1
# O(n) | O(n)

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        hashmap = {}

        text = list(text)
        balloon = list('balloon')

        for c in text:
            if c in balloon:
                if c in hashmap:
                    hashmap[c] += 1
                else:
                    hashmap[c] = 1


        if len(hashmap) < 5:
            return 0 


        hashmap['l1'] = hashmap['l'] // 2
        hashmap['l']//=2

        hashmap['o1'] = hashmap['o'] // 2
        hashmap['o']//=2


        return min(hashmap.values())