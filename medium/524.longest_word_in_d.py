class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        #fast
        for x in sorted(d, key=lambda x: (-len(x), x)):
            it = iter(s)
            if all(c in it for c in x):
                return x
        return ''


        #python sort 是稳定的，有相同的key时，前后顺序不变
        #method_1
        #mine
        d.sort()
        d.sort(key = len,reverse = True)

        #method_2
        d.sort(key = lambda x: (-len(x), x))
        
                
        for word in d:
            i = 0
            for char in s:
                if i < len(word) and word[i] == char:
                    i += 1

            if i == len(word):
                return word
        
        return ""



        

s = Solution()
a = s.findLongestWord("abpcplea",["ale","apple","monkey","plea","applf"])
print(a)     

        

