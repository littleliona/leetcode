import collections
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = collections.Counter(s)
        res = []
        res.extend( ['0'] * dic.get('z', 0) )
        res.extend( ['1'] * (dic.get('o', 0)-dic.get('z', 0)-dic.get('w', 0)-dic.get('u', 0)) )
        res.extend( ['2'] * dic.get('w', 0) )
        res.extend( ['3'] * (dic.get('h', 0)-dic.get('g', 0)) )
        res.extend( ['4'] * dic.get('u', 0) )
        res.extend( ['5'] * (dic.get('f', 0)-dic.get('u', 0)) )
        res.extend( ['6'] * dic.get('x', 0) )
        res.extend( ['7'] * (dic.get('s', 0)-dic.get('x', 0)) )
        res.extend( ['8'] * dic.get('g', 0) )
        res.extend( ['9'] * (dic.get('i', 0)-dic.get('g', 0)-dic.get('x', 0)-dic.get('f', 0)+dic.get('u', 0) ) )
        return ''.join(res)



s = Solution()
a = s.originalDigits("owoztneoer")
print(a)     

        

