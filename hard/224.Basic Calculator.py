class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        i = 0
        sign = 1
        stack = []

        while i < len(s):
            if s[i].isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                res += sign * int(s[start:i])
                continue
            elif s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == '(':
                stack.append((res,sign))
                res = 0
                sign = 1
            elif s[i] == ')':
                res_before, sign_before = stack.pop()
                res = res_before + sign_before * res
            i += 1
        return res


s = Solution()
a = s.longestValidParentheses(')()())')
print(a)
