class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        #查找数值插入的位置，bisect_left重复数值最左侧，bisect_right重复数值最右侧
        left = right = bisect.bisect_left(arr, x)
        while right - left < k:
            # left下界，right上界
            # 可能数组越界，直接返回
            if left == 0: return arr[:k]
            if right == len(arr): return arr[-k:]
            #调整数值，偏好左侧更小值
            if x - arr[left - 1] <= arr[right] - x: left -= 1
            else: right += 1
        return arr[left:right]

s = Solution()
a = s.findClosestElements()
print(a)
