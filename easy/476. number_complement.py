class Solution(object):
    def findComplement(self, num):
    	#mine
        str1 = bin(num)
        str2 = str1[2:]
        str2 = str2.replace('1','2')
        str2 = str2.replace('0','1')
        str2 = str2.replace('2','0')
        return int(str2,2)
        #easy
        i = 1
        while i <= num:
            i = i << 1
        return (i - 1) ^ num