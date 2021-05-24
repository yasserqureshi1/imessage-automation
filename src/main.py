import subprocess
from shlex import quote
import time

def send(phone, message, dir_path):
    relative_path = 'send_message.js'
    path = f'{dir_path}/{relative_path}'
    cmd = f'osascript -l JavaScript {path} {quote(phone)} {quote(message)}'
    subprocess.call(cmd, shell=True)

    
n = 3
while n>0:
    print(f'Sending message {n}')
    PHONE_NUMBER = '00'
    MESSAGE = 'This is an automated message'
    DIR_PATH = ''
    send(phone=PHONE_NUMBER, message=MESSAGE, dir_path=DIR_PATH)
    time.sleep(0.1)
    n -= 1
