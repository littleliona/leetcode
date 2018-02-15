class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """

        if len(num) < 3:
            return False
        l = len(num)
        for i in range(1,len(num) // 2 + 1):
            if num[0] == '0' and i >= 2:
                break

            j = i + 1
            while l-j >= max(j-i,i):
                if num[i] == '0' and j - i >= 2:
                    break

                if self.check_valid(num[:i],num[i:j],num[j:]):
                    return True

                j += 1
        return False

    def check_valid(self, n1, n2, remain):
        if not remain:
            return True

        s = int(n1) + int(n2)
        
        if not remain.startswith(str(s)):
            return False

        return self.check_valid(n2, str(s), remain[len(str(s)):])

        
if __name__ == '__main__':
    s = Solution()
    a = s.isAdditiveNumber("199100199")
    print(a)
