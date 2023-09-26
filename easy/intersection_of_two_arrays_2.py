# Solution 1
# O(n^2) | O(n)

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        output = []

        if len(nums1) < len(nums2):
            smaller = nums1
            larger = nums2
        else:
            smaller = nums2
            larger = nums1
        
        for num in smaller:
            if num in larger:  
                larger.remove(num)
                output.append(num)

        return output