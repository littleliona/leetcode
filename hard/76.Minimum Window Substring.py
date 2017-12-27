import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #method_1
        MAX_INT = 2147483647
        start = end = 0
        char_need = defaultdict(int)    # the count of char needed by current window, negative means current window has it but not needs it
        count_need = len(t)             # count of chars not in current window but in t
        min_length = MAX_INT
        min_start = 0
        for i in t:
            # current window needs all char in t
            char_need[i] += 1           
        while end < len(s):
            if char_need[s[end]] > 0:
                count_need -= 1
            # current window contains s[end] now, so does not need it any more
            char_need[s[end]] -= 1      
            end += 1
            while count_need == 0:
                if min_length > end - start:
                    min_length = end - start
                    min_start = start
                # current window does not contain s[start] any more
                char_need[s[start]] += 1    
                # when some count in char_need is positive, it means there is char in t but not current window
                if char_need[s[start]] > 0: 
                    count_need += 1
                start += 1
        return "" if min_length == MAX_INT else s[min_start:min_start + min_length]

        #method_2
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j

        return s[I:J]

s = Solution()
a = s.minWindow("ADOBECODEBANC","ABC")
print(a)
