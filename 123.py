import hashlib

# by reaper666

print("1: MD5")
print("2: SHA1")
print("3: SHA224")
print("4: SHA256")
print("5: SHA384")
print("6: SHA512")
print("7: Blake2b")
print("8: Blake2s")

num = int(input("Select the appropriate option"))
if 1 > num or num > 8:
    print("Error")
else:
    inp = input("OK, now enter the string whose hash you need")
    if num == 1:
        print(hashlib.md5(inp.encode('utf-8')).hexdigest())
    elif num == 2:
        print(hashlib.sha1(inp.encode('utf-8')).hexdigest())
    elif num == 3:
        print(hashlib.sha224(inp.encode('utf-8')).hexdigest())
    elif num == 4:
        print(hashlib.sha256(inp.encode('utf-8')).hexdigest())
    elif num == 5:
        print(hashlib.sha384(inp.encode('utf-8')).hexdigest())
    elif num == 6:
        print(hashlib.sha512(inp.encode('utf-8')).hexdigest())
    elif num == 7:
        print(hashlib.blake2b(inp.encode('utf-8')).hexdigest())
    elif num == 8:
        print(hashlib.blake2s(inp.encode('utf-8')).hexdigest())
