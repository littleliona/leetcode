class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
        n = len(citations)
        l = 0; r = n-1
        
        while l <= r:
            mid = (l+r)/2
            if citations[mid] == n-mid:
                return n-mid
            elif citations[mid] < n-mid:
                l = mid+1
            else:
                r = mid-1
                
        return n-l
        

s = Solution()
a = s.hIndex([1,4,4,4,4,4])
print(a)
