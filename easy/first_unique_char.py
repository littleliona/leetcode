from functools import reduce
import operator
import string
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        min_ = len(s)
        for s_ in set(s):
            if s.count(s_) == 1:
                min_ = min(min_,s.index(s_))

        if min_ == len(s):
            return -1
        else:
            return min_


s = Solution()
a = s.firstUniqChar("aabb")
print(a)