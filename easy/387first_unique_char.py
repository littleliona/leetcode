from functools import reduce
import operator
import string
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        #mine
        min_ = len(s)
        for s_ in set(s):
            if s.count(s_) == 1:
                min_ = min(min_,s.index(s_))

        if min_ == len(s):
            return -1
        else:
            return min_

        #easy
        return min([s.find(c) for c in string.ascii_lowercase if s.count(c)==1]) or [-1]


s = Solution()
a = s.firstUniqChar("aabb")
print(a)