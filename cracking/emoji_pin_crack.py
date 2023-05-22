import hashlib

for i in range(1000000):
    pin = '{:06d}'.format(i)
    plaintext = '🚎🍕🎥💔' + pin
    check = hashlib.md5(plaintext.encode())
    check = hashlib.sha1(check.hexdigest().encode())
    check = hashlib.md5(check.hexdigest().encode())
    check = hashlib.sha1(check.hexdigest().encode())
    check = hashlib.md5(check.hexdigest().encode())
    check = hashlib.sha1(check.hexdigest().encode())
    check = hashlib.md5(check.hexdigest().encode())
    check = hashlib.sha1(check.hexdigest().encode())
    if str(check.hexdigest()) == '0124e205fbd3f391a4e7e3b20e05b962d360bdd9':
        print(pin)