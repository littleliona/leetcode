class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def is_valid(s):
            cnt = 0
            for char in s:
                if char == '(':
                    cnt += 1
                elif char == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False

            return cnt == 0

        level = {s}
        while True:
            valid = filter(is_valid,level)
            if valid:
                return valid

            level = {s[:i]+s[i+1:] for s in level for i in range(len(s))}

if __name__ == '__main__':
    s = Solution()
    a = s.isAdditiveNumber("199100199")
    print(a)
