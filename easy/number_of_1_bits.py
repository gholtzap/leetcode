class Solution:
    def hammingWeight(self, n: int) -> int:  
        # convert to binary 
        binary = format(n,'b')
        # convert to string then count how many 1's
        output = str(binary).count('1')

        return output