class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        #best
        len_=0
        flag = False
        for s_ in set(s):
            if s.count(s_)%2 ==0:
                len_+=s.count(s_)
            else:
                len_+=s.count(s_)-1
                flag = True

        return len_+1 if flag else len_

        #easy
        odds = sum(v & 1 for v in collections.Counter(s).values())
        return len(s) - odds + bool(odds)





s = Solution()
a = s.containsDuplicate([1,2,3,2])
print(a)