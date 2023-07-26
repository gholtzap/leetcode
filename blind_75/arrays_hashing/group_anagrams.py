# Solution 1

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()
    
    
# Solution 2
# O(n^2 log(n)) | O(n)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        output,hashmap = [],{}

        for i,x in enumerate(strs):
            x = list(x)
            x.sort()
            x = "".join(x)
            if x not in hashmap:
                hashmap[x] = [i]
            else:
                hashmap[x].append(i)

        for x in hashmap:
            temp = []
            for y in hashmap[x]:
                temp.append(strs[y])
            output.append(temp)

        return output