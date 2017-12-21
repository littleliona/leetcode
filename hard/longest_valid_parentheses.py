class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0 for _ in range(len(s)+1)]
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    p = stack.pop()
                    dp[i+1] = dp[p] + i - p + 1
        
        return max(dp)
s = Solution()
a = s.longestValidParentheses(')()())')
print(a)
