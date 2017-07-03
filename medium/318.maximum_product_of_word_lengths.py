class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        #因为只包含小写字母，int类型为32位，所以可以用后26位来对应26个字母
        #如果该位为1，代表该位置的字幕出现
        #计算1<<ord(char)-ord('a')表示出现的字符在第几位上
        #通过｜运算得到最终的字符（重复字符只表示一次，所以用了set），存入字典中
        #遍历字典，如果两个mask&为0，说明不相交
        d = {}
        for w in words:
            mask = 0
            for c in set(w):
                mask |= (1 << (ord(c) - 97))
            d[mask] = max(d.get(mask, 0), len(w))
        return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])


        
    

s = Solution()
a = s.maxProduct(["a", "aa", "aaa", "aaaa"])
print(a)     

        

