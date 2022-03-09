import hashlib

for i in range(1000000):
    pin = '5260452f' + '{:06d}'.format(i)
    check = hashlib.md5(pin.encode())
    if str(check.hexdigest()) == '5cdacc3ed69889ee8390d44a5381e7b0':
        print(pin)