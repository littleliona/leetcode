from collections import defaultdict
from collections import Counter
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic_ = {}

        for string in strs:
            key = tuple(sorted(string))
            dic_[key] = dic_.get(key,[]) + [string]

        return dic_.values()

s = Solution()
a = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(a)
