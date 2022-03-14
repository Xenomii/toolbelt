import hashlib

for i in range(1000000):
    pin = '{:06d}'.format(i)
    plaintext = '5260452f' + pin
    check = hashlib.md5(plaintext.encode())
    if str(check.hexdigest()) == '5cdacc3ed69889ee8390d44a5381e7b0':
        print(pin)