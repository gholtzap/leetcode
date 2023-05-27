# Solution 1
# O(n^2) | O(n)

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        dictionary = {}

        for domainKey in cpdomains:
            domainSplit = domainKey.replace(' ','.').split('.')
            
            domainExtension = domainSplit[-1]
            timesVisited = int(domainSplit[0])

            if domainExtension not in dictionary:
                dictionary[domainExtension] = timesVisited
            else:
                dictionary[domainExtension] += timesVisited

            tempStr = ""
            for x in range(len(domainSplit)-2,0,-1):
                tempStr = domainSplit[x]+'.' + tempStr

                domainWithExtension = tempStr + domainExtension

                if domainWithExtension not in dictionary:
                    dictionary[domainWithExtension] = timesVisited
                else:
                    dictionary[domainWithExtension] += timesVisited

            output = []
            for val in dictionary:
                output.append(str(dictionary[val])+" "+val)

        return output
