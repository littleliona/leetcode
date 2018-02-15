class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder = preorder.split(',')

        stack = []
        for pre in preorder:
            stack.append(pre)
            while len(stack) >= 2 and stack[-1] == '#' and stack[-2] == '#' :
                stack.pop()
                stack.pop()
                if stack:
                    stack[-1] = '#'
                else:
                    return False

        return len(stack) == 1 and stack[-1] == '#'








if __name__ == '__main__':
    s = Solution()
    a = s.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")
    print(codec.serialize(root))