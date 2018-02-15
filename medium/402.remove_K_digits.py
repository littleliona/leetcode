class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        n = k
        for i in range(len(num)):
            while stack and stack[-1] > num[i] and n > 0:
                n -= 1
                stack.pop()
            stack.append(num[i])

        stack = stack[:len(num)-k]
        while stack and stack[0] == '0':
            stack.pop(0)

        return ''.join(stack) if stack else '0'



if __name__ == '__main__':
    s = Solution()
    a = s.removeKdigits("1173",2)
    print(a)
