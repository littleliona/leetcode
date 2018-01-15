class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        cur = []
        res = []
        num_letters = 0

        for word in words:
            if len(word) + len(cur) + num_letters > maxWidth:
                if len(cur) == 1:
                    res.append( cur[0] + ' '*(maxWidth - num_letters))
                else:
                    num_space = maxWidth - num_letters
                    add_space ,extra_space = divmod(num_space, len(cur)-1)
                    for i in range(extra_space):
                        cur[i] += ' '

                    res.append((' '*add_space).join(cur))
                cur = []
                num_letters = 0
            cur += [word]
            num_letters += len(word)

        res.append(' '.join(cur) + ' ' * (maxWidth - num_letters - len(cur) + 1))
        return res

s = Solution()
a = s.fullJustify([""],0)
print(a)
