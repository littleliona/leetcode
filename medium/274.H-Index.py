class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
        citations.sort()
        max_h = 0

        for i,citation in enumerate(citations):
            max_h = max(max_h, min(citation, len(citations)-i))

        return max_h


s = Solution()
a = s.hIndex([1,4,4,4,4,4])
print(a)
