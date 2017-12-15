class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not n:
            return 1

        if n < 0:
            return 1/self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)

        
        return self.myPow(x*x, n//2) 


s = Solution() 
a = s.multiply([-1,0,1,2,-1,-4])
print(a)

