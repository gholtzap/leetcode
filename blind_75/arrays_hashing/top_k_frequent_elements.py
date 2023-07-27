# Solution 1
# O(n log n) | O(n)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums.sort()
        temp,output = [],[]

        hashmap = {}

        for x in nums:
            if x not in hashmap:
                hashmap[x]=1
            else:
                hashmap[x]+=1

        for x in hashmap:
            temp.append([hashmap[x],x])

        temp.sort()

        for i in range(len(temp)-1,len(temp)-1-k,-1):
            output.append(temp[i][1])

        return output