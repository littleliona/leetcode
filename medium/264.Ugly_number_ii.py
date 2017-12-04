class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 从1开始扩展ugly number, 分别 *2，*3，*5
        # 选中最小的，然后向后移动一步
        q = [1]
        i2 = i3 = i5 = 0
        while len(q) < n:
            m2, m3, m5 = q[i2] * 2, q[i3] * 3, q[i5] * 5
            m = min(m2, m3, m5)
            if m == m2:
                i2 += 1
            if m == m3:
                i3 += 1
            if m == m5:
                i5 += 1
            q += m,
        
        return q[-1]

                
s = Solution()
a = s.nthUglyNumber(3)
print(a)
