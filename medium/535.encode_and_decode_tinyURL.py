class Codec:

    #faster 
    #two dic: one to encode one to decode
    #design pattern: 后面加上随机抽取出来的6个字符
    alphabet = string.ascii_letters + '0123456789'

    def __init__(self):
        self.encodeurl = {}
        self.decodeurl = {}

    def encode(self, longUrl):
        while longUrl not in self.encodeurl:
            code = ''.join(random.choice(Codec.alphabet) for _ in range(6))
            if code not in self.decodeurl:
                self.encodeurl[longUrl] = code
                self.decodeurl[code] = longUrl

        return 'http://tinyurl.com/' + self.encodeurl[longUrl]

    def decode(self, shortUrl):
        return self.decodeurl[shortUrl[-6:]]

 
    #easy to understand
    #每个url放入list中，返回在list中的下标，设计成shorturl
    #decode:根据下标找到url
    def __init__(self):
        self.urls = []

    def encode(self, longUrl):
        self.urls.append(longUrl)
        return 'http://tinyurl.com/' + str(len(self.urls) - 1)

    def decode(self, shortUrl):
        return self.urls[int(shortUrl[-1])]

# Your Codec object will be instantiated and called as such:
codec = Codec()
print(codec.encode('https://leetcode.com/problems/design-tinyurl'))
print(codec.decode('http://tinyurl.com/0'))
        

'''    
s = Solution()
a = s.countAndSay(4)
print(a)
'''