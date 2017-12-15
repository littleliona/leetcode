class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1 or len(s) <= numRows:
            return s

        index, step = 0,1
        
        L = [''] * numRows 
        for char in s:
            L[index] += char 
            if index == 0:
                step = 1
            if index == numRows - 1:
                step = -1

            index += step

        return ''.join(L)
           

