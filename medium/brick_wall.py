# Solution 1
# O(n^2) | O(n)

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        hashmap,nums = {},[]
        sum_row = sum(wall[0])

        for row in wall:
            tempSum = 0
            for column in range(len(row)):
                tempSum+=row[column]
                if tempSum not in hashmap and tempSum != sum_row:
                    hashmap[tempSum] = 1
                elif tempSum in hashmap and tempSum != sum_row:
                    hashmap[tempSum] +=1
        
        for x in hashmap:
            nums.append(hashmap[x])

        if not hashmap:
            return len(wall)
        else:
            return len(wall) - max(nums)