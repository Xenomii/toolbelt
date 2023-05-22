import hashlib

for i in range(1000000):
    pin = '{:06d}'.format(i)
    plaintext = '0b9fd0cd' + pin
    check = hashlib.md5(plaintext.encode())
    if str(check.hexdigest()) == 'cba765ace2e797f73a182c37ad7a7613':
        print(pin)