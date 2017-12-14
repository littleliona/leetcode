class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #method_answer
        max_len, start = 0, 0
        seen = {}

        for i in range(len(s)):
            if s[i] in seen and start <= seen[s[i]]:
                start = seen[s[i]] + 1
            else:
                max_len = max(max_len, i - start + 1)
            seen[s[i]] = i

        return max_len

        #mine
        if not s:
            return 0

        max_length = 0
        L = [s[0]]
        for i,char in enumerate(s):
            if char in L:
                index = L.index(char)
                L = L[index+1:]

            L.append(char)
            max_length = max(max_length,len(L))

        return max_length

s = Solution()
a = s.lengthOfLongestSubstring('pwwkew')
print(a)
