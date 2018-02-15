class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        #method_1
        if n == 1:
            return 0
        if n % 2 == 0:
            return 1 + self.integerReplacement(n//2)
        
        return 1 + min(self.integerReplacement(n+1),self.integerReplacement(n-1))

        #method_2
        if n < 1:
            return -1
        check = {}
        return self.helper(n, check)
    
    def helper(self, n, check):
        if n in check:
            return check[n]
        if n == 1:
            return 0
        if n % 2 == 0:
            check[n] = self.helper(n / 2, check) + 1
            return check[n]
        check[n] = min(self.helper(n+1, check), self.helper(n-1, check)) + 1
        return check[n]        



if __name__ == '__main__':
    s = Solution()
    a = s.integerReplacement(7)
    print(a)
