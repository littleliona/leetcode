import collections
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #mine
        count = 0

        if k>0:
            nums1 = [n+k for n in set(nums)]
            return len(set(nums1)&set(nums))    
        elif k==0:
            v = collections.Counter(nums)
            for key in v:
                if v[key] > 1:
                    count += 1
        
        return count

        #same idea -- more concise
        #attention to the Counter().values()
        if k>0:
            return len(set(nums)&set(n+k for n in nums))
        elif k==0:
            return sum(v>1 for v in collections.Counter(nums).values())
        else:
            return 0


s = Solution()
a = s.findPairs([1, 1, 2, 2, 5],1)
print(a)
    


        





