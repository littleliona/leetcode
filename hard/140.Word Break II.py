class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        memo = {len(s): ['']}
        def sentences(i):
            if i not in memo:
                memo[i] = []
                for j in range(i+1, len(s)+1):
                    if s[i:j] in wordDict:
                        for tail in sentences(j):
                            if tail != '':                                
                                memo[i].append( s[i:j] + ' ' + tail)
                            else:
                                memo[i].append( s[i:j] )
            return memo[i]
        return sentences(0)


if __name__ == '__main__':
    s = Solution()
    a = s.wordBreak("leetcode",["leet", "code"])
    print(a)
