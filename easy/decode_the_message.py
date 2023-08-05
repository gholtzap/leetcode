# Solution 1
# O(n) | O(n)

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:

        hashmap,step = {},""

        val,key = 0,list(key)

        for x in key:
            if x == ' ':
                step+=" "
            elif x not in hashmap:
                step+= x
                hashmap[x] = 97+val
                val+=1
        
        output = ""

        for x in message:
            if x != ' ':
                output+= chr(hashmap[x])
            else:
                output+= " "

        return output
