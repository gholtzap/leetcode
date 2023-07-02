# Solution 1
# O(log(n)) | O(1)

class Solution:
    def trailingZeroes(self, n: int) -> int:
        x,r=5,0
        while x<=n:
            r+=n//x
            x*=5
        return r


# Solution 2
# O(n) | O(n)

class Solution:
    def trailingZeroes(self, n: int) -> int:

        n = math.factorial(n)
        if n > 1000000:
            sys.set_int_max_str_digits(55 * 4300)
        lst = list(str(n))

        output = 0
        for i in range(len(lst)-1,0,-1):
            if lst[i] == '0':
                output+=1
                continue
            return output

        return output