class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def is_palindrome(word):
            return word == word[::-1]

        res = []
        
        dic = {word:i for i,word in enumerate(words)}

        
        for k,word in enumerate(words):
            n = len(word)
            if is_palindrome(word) and "" in words and word != "":
                res.append([dic[""],k])
                res.append([k,dic[""]])

            if word[::-1] in dic and dic[word[::-1]] != k:
                res.append([k,dic[word[::-1]]])

            for i in range(1,n):
                prefix = word[:i]
                suffix = word[i:]

                if is_palindrome(prefix):
                    back = suffix[::-1]
                    if back in dic:
                        res.append([dic[back],k])
                if is_palindrome(suffix):
                    back = prefix[::-1]
                    if back in dic:
                        res.append([k,dic[back]])

        return res
        
if __name__ == '__main__':
    s = Solution()
    a = s.palindromePairs(["aaa","b","aaa"])
    print(a)
