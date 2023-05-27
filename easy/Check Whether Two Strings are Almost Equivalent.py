# Solution 1 
# O(n) | O(n)

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:

        charCount = {}

        for x in word1:
            if x not in charCount:
                charCount[x]=1
                continue
            charCount[x]+=1

        word2 = list(word2)

        for y in word2:
            count1 = word1.count(y)
            count2 = word2.count(y)

            if y not in charCount:
                if word2.count(y) - 3 > 0:
                    return False
            if max(count1,count2) - min(count1,count2) > 3:
                return False

        for y in word1:
            count1 = word1.count(y)
            count2 = word2.count(y)

            if y not in charCount:
                if word2.count(y) - 3 > 0:
                    return False
            if max(count1,count2) - min(count1,count2) > 3:
                return False
         
        return True