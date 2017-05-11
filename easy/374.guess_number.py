# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num):
    if num < 6:
        return 1
    if num > 6:
        return -1
    if num == 6:
        return 0

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        #折半查找 
        #notice the return value of guess(num)
        #e.p:-1 means my number is lower , num > picked value
        start = 1
        end = n
        if guess(n) == 0:
            return n
        while start<end:
            mid = start + (end - start) // 2
            if guess(mid) == -1:
                end = mid-1
            elif guess(mid) == 0:
                return mid
            else:
                start = mid+1
        return start

        
s = Solution()
a = s.guessNumber(10)
print(a)



