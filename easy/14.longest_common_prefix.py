class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #easy and fast
        if not strs:
            return ""

        #zip(*strs)
        #e.m.:strs = ['aaa','bbbb','cccc']
        #zip(*strs) = ['abc,'abc','abc']
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:      
                return strs[0][:i]
        
        return min(strs)   #最长公共前缀为长度最短的字符串
        
        #mine
        if not strs:
            return ""

        if len(strs) == 1:
            return strs[0]
        
        s = strs[0]
        flag = True
        min_ = len(strs[0])
        for str_ in strs:
            if len(str_)< min_:
                min_ = len(str_)
                s = str_
        
        i = 0
        for i,char in enumerate(s):
            for str_ in strs:
                if str_[i]!= char:
                    flag = False
                    break
            if not flag:
                break

        if flag:
            return s
        else:
            return s[:i] if i!=0 else ""
            


        
s = Solution()
a = s.longestCommonPrefix(["aba","abab","ababa"])
print(a)