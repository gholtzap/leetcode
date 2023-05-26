# Solution 1
# O(n) | O(n)

class Solution:
    def reverseVowels(self, s: str) -> str:
        l,r = 0, len(s)-1
        sList =list(s)
        vowels = set("aeiouAEIOU")

        while l<r:
            if sList[l] in vowels and sList[r] in vowels:
                sList[l],sList[r]=sList[r],sList[l]
                l+=1
                r-=1
            elif sList[l] in vowels and not sList[r] in vowels:
                r-=1
            elif not sList[l] in vowels and sList[r] in vowels:
                l+=1
            else:
                l+=1
                r-=1
        return ''.join(sList)
    

# Solution 2 (just solution 1 but slightly worse)
# O(n) | O(n)

class Solution:
    def reverseVowels(self, s: str) -> str:
        l,r = 0, len(s)-1
        sList =list(s)
        while l<r:
            temp=''
            if isVowel(sList[l]) and isVowel(sList[r]):
                
                
                temp = sList[r]
                sList[r] = sList[l]
                sList[l] = temp
                l+=1
                r-=1
            elif isVowel(sList[l]) and not isVowel(sList[r]):
                r-=1
            elif not isVowel(sList[l]) and isVowel(sList[r]):
                l+=1
            else:
                l+=1
                r-=1
        return ''.join(sList)

def isVowel(c: chr) -> bool:
    cLower = c.lower()
    if cLower == 'a' or cLower == 'e' or cLower == 'i' or cLower == 'o' or cLower == 'u':
        return True