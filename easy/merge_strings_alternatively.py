class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        output,index = "",0

        while(index < min(len(word1),len(word2))):
            output+=word1[index] + word2[index]
            index+=1

        output+= word1[index:] if len(word1) > len(word2) else word2[index:]

        return output