class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        #d[i] is True if there is a word in the dictionary that ends at ith index of s 
        #AND d is also True at the beginning of the word
        d = [False] * len(s)    
        for i in range(len(s)):
 		    for w in wordDict:
 			    if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
 				    d[i] = True
        
        return d[-1]

        

s = Solution()
a = s.wordBreak("leetcode",["leet", "code"])
print(a)
