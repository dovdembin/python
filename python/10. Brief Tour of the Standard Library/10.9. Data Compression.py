import zlib
s = b'witch which has which witches wrist watch'
print(len(s))  # 41

t = zlib.compress(s)
print(len(t))  # 37

print(zlib.decompress(t))  # b'witch which has which witches wrist watch'

print(zlib.crc32(s))  # 226805979
