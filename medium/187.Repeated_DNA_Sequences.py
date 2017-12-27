class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        #method_1
        res = set()
        track = set()

        for i in range(len(s)-9):
            seq = s[i:i+10]
            if seq in track:
                res.add(seq)
            else:
                track.add(seq)

        return list(res)
        
        #method_2
        dic = {}

        for i in range(len(s)-9):
            seq = s[i:i+10]
            if seq not in dic:
                dic[seq] = 1
            else:
                dic[seq] += 1

        return [key for key,value in dic.items() if value > 1]

s = Solution()
a = s.longestValidParentheses(')()())')
print(a)
