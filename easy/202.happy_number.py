class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #mine
        sum = 0
        L = []
        while True:
            while n>=10:
                sum += (n%10) **2
                n = n//10
            sum += n**2
            if sum == 1:
                return True
            else:
                if sum in L:
                    return False
                else:
                    n = sum
                    L.append(sum)
                    sum = 0
        #easy
        mem = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in mem:
                return False
            else:
                mem.add(n)
        else:
            return True

s = Solution()
a = s.isHappy(19)
print(a)