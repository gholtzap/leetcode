# Easiest solution: (kinda cheating)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()
        return nums[0]


# To do this prblem authentically, basically we need to replace nums.sort() with the most efficient sorting algorithm.
# We can use quicksort like so:
# Keep in mind that although this is more efficient on larger samples, the leetcode testcases are small and prefer binary sort

class Solution:
    def findMin(self, nums: List[int]) -> int:

        return quicksort(nums)[0]


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()

    items_greater = []
    items_lower = []

    for item in arr:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quicksort(items_lower) + [pivot] + quicksort(items_greater)