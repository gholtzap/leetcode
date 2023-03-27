class Solution(object):
    def convert(self, s, numRows):
        if numRows==1:
          return s
        
        # use list for improved memory usage compared to str
        output = []

        for i in range(numRows):
          j = 2*(numRows-1)
          for k in range(i, len(s), j):
            output.append(s[k])
            if(i>0 and i<numRows-1 and k+j-2*i<len(s)):
              output.append(s[k+j-2*i])

        return ''.join(output)