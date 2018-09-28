#! /usr/bin/env python
# http://www.cnblogs.com/alex3714/articles/5161349.html
import hashlib
import hmac

m = hashlib.md5()
m.update(b"Hello")
m.update(b"It's me")
print(m.digest())
m.update(b"It's been a long time since last time we ...")

print(m.digest())  # 2进制格式hash
print(len(m.hexdigest()))  # 16进制格式hash
'''
def digest(self, *args, **kwargs): # real signature unknown
    """ Return the digest value as a string of binary data. """
    pass

def hexdigest(self, *args, **kwargs): # real signature unknown
    """ Return the digest value as a string of hexadecimal digits. """
    pass

'''

# ######## md5 ########

hash1 = hashlib.md5()
hash1.update(b'admin')
print(hash1.hexdigest())

# ######## sha1 ########

hash2 = hashlib.sha1()
hash2.update(b'admin')
print(hash2.hexdigest())

# ######## sha256 ########

hash3 = hashlib.sha256()
hash3.update(b'admin')
print(hash3.hexdigest())

# ######## sha384 ########

hash4 = hashlib.sha384()
hash4.update('admin'.encode(encoding='utf-8'))
print(hash4.hexdigest())

# ######## sha512 ########

hash5 = hashlib.sha512()
hash5.update(b'admin')
print(hash5.hexdigest())


# ######## hmac ########
h = hmac.new('天王盖地虎'.encode(encoding='utf-8'), '宝塔镇河妖'.encode(encoding='utf-8'))
print(h.hexdigest())
print(h.digest())