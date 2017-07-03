class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack = []
        for char in s:
            range_ = -1 if not stack else stack[-1]   #确定查找范围，每一次都在上个字符index后查找，确保顺序正确
            list_new = t[range_+1:]                   #切片
            if char in list_new:
                stack.append(list_new.index(char) + range_+1)    #找到对应字符的index
        

        return len(stack) == len(s)


 
s = Solution()
a = s.isSubsequence()
print(a)     

        

