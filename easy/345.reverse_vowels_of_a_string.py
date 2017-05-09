class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        #mine
        L = ['a','e','i','o','u','A','E','I','O','U']
        L_index = []
        L_char = []
        L_str = list(s)
        count = 0
        for i,char in enumerate(s):
            if char in L:
                L_index.append(i)
                L_char.append(char)
                count+=1

        L_char = L_char[::-1]
        for m in range(count):
            L_str[L_index[m]] = L_char[m]

        return "".join(L_str)

        #easy
        vowels = set(list("aeiouAEIOU"))
        s = list(s)
        ptr_1, ptr_2 = 0, len(s) - 1
        while ptr_1 < ptr_2:
            if s[ptr_1] in vowels and s[ptr_2] in vowels:
                s[ptr_1], s[ptr_2] = s[ptr_2], s[ptr_1]
                ptr_1 += 1
                ptr_2 -= 1
            if s[ptr_1] not in vowels:
                ptr_1 += 1
            if s[ptr_2] not in vowels:
                ptr_2 -= 1
        return ''.join(s)

s = Solution()
a = s.reverseVowels("leetcode")
print(a)