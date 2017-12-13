from collections import defaultdict
from collections import Counter
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        for char in set(s):
            if s.count(char) < k:
                return max(self.longestSubstring(t, k) for t in s.split(char))

        return len(s)
        
s = Solution()
a = s.longestSubstring('ababbc',2)
print(a)
