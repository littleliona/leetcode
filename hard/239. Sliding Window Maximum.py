import collections
class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq = collections.deque()
        
        for i in range(len(nums)):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if dq[0] == i-k:
                dq.popleft()
            if i >= k - 1:
                res.append(dq[0])

        return res

if __name__ == '__main__':
    s = Solution()
    a = s.wordBreak("leetcode",["leet", "code"])
    print(a)
