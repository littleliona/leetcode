class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #dict  stack
        stack = []
        dic = {"[":"]","{":"}","(":")"}
        for char in s:
            if char in dic.keys():
                stack.append(char)
            elif char in dic.values():
                if not stack or dic[stack.pop()]!=char:
                    return False
            else:
                return False

        return not stack

        #mine  stack list
        left = ['(','{','[']
        right = [')','}',']']

        stack = []
        check = ''

        for char in s:
            if char in left:
                stack.append(char)
            else:
                if stack:
                    check = stack.pop()
                    if left.index(check) != right.index(char):
                        return False
                else:
                    return False

        return True if not stack else False
        
        
s = Solution()
a = s.isValid('([])')
print(a)