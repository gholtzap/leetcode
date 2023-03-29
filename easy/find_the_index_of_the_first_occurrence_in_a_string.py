class Solution(object):
    def strStr(self, haystack, needle):
       
        if haystack.count(needle) == 0:
            return -1
        else:
            return haystack.index(needle)