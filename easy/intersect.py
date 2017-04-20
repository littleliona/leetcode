import collections
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #mine
        L = list(set(nums1)&set(nums2))
        L1 = []
        for n in L:
            min_=min(nums1.count(n),nums2.count(n))
            for m in range(min_):
                L1.append(n)
        return L1
        
        #easy_1
        c1, c2 = collections.Counter(nums1), collections.Counter(nums2)
        return sum([[num] * min(c1[num], c2[num]) for num in c1 & c2], [])
        #easy_2
        a, b = map(collections.Counter, (nums1, nums2))
        return list((a & b).elements())


s = Solution()
a = s.intersect([1,2,2,1],[2,2])
print(a)