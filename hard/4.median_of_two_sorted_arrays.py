class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len_1 = len(nums1)
        len_2 = len(nums2)
        
        if (len_1+len_2) % 2 == 1:
            return self.getKth(nums1, nums2, (len_1+len_2)//2 + 1)

        else:
            return (self.getKth(nums1, nums2, (len_1+len_2)//2) + self.getKth(nums1, nums2, (len_1+len_2)//2 + 1)) / 2

    def getKth(self, nums1, nums2, k):
        len_1 = len(nums1)
        len_2 = len(nums2)

        if len_1 > len_2:
            return self.getKth(nums2, nums1, k)
        
        if len_1 == 0:
            return nums2[k-1]

        if k == 1:
            return min(nums1[0], nums2[0])


        pa = min(len_1, k//2)
        pb = k - pa

        if nums1[pa-1] <= nums2[pb-1]:
            return self.getKth(nums1[pa:], nums2, pb)
        else:
            return self.getKth(nums1, nums2[pb:], pa)
