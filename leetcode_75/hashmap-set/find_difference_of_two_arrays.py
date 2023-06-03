# Solution 1
# O(n^2) | O(n)

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:


        hashset1 = set(nums1)
        hashset2 = set(nums2)

        output1,output2 = [],[]

        for x in nums1:
            if x not in hashset2 and x not in output1:
                output1.append(x)

        for x in nums2:
            if x not in hashset1 and x not in output2:
                output2.append(x)


        return [output1,output2]
    


# Solution 2
# O(n) | O(n)

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        output1,output2 = [],[]
   
        hashset1 = set(nums1)
        hashset2 = set(nums2)

        test = list(hashset1.symmetric_difference(hashset2))
        
        for x in test:
            if x not in hashset1:
                output2.append(x)
            if x not in hashset2:
                output1.append(x)

        return [output1,output2] 
            
            
# Solution 3
# O(n) | O(n)

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:


        hashset1 = set(nums1)
        hashset2 = set(nums2)

        output1,output2 = set(),set()

        for x in nums1:
            if x not in hashset2 and x not in output1:
                output1.add(x)

        for x in nums2:
            if x not in hashset1 and x not in output2:
                output2.add(x)


        return [list(output1),list(output2)]