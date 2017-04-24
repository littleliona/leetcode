class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for note in set(ransomNote):
            if ransomNote.count(note) > magazine.count(note):
                return False

        return True



s = Solution()
a=s.canConstruct("aa","ab")
print(a)