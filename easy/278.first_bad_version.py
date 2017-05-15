# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        #binary_search
        start = 1
        end = n

        while start < end:
            mid = start + (end - start)/2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid+1

        return start


        
s = Solution()
a = s.rotate([1,2],1)
print(a)



