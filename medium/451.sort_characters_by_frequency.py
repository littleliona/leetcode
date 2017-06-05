#from collections import Counter
import collections
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        #mine
        s1 = ""
        dic = Counter(s)
        L = sorted(dic.items(),key = lambda x:x[1],reverse = True)
        for i in L:
            s1 += i[0]*i[1]

        return s1
        
        #one-line
        return "".join([char * times for char, times in collections.Counter(s).most_common()])

        
        


        
s = Solution()
a = s.frequencySort("tree")
print(a)
