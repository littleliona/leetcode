class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z == 0:
            return True
        
        return (z <= x + y and z %self.gcd(x,y) == 0)
    def gcd(self,x,y):
        if y == 0:
            return x
        return self.gcd(y , x%y)



if __name__ == '__main__':
    s = Solution()
    a = s.canMeasureWater(5,6,34)
    print(a)
