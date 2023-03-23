class Solution:
    # since the 6 closest to the left will always have the highest value,
    # we always want to replace the 'first 6'.
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace('6', '9', 1))