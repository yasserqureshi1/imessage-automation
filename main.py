import subprocess
import sys
from shlex import quote
import time

def send(phone, message, dir_path):
    #dir_path = os.path.dirname(os.path.realpath(__file__))
    #dir_path = os.path.normpath(join(os.getcwd(), path))
    #dir_path = os.path.dirname(sys.argv[0])
    relative_path = 'send_message.js'
    path = f'{dir_path}/{relative_path}'
    cmd = f'osascript -l JavaScript {path} {quote(phone)} {quote(message)}'
    subprocess.call(cmd, shell=True)

    
n = 100
while n>0:
    phone_number = ''
    message = 'pick up ur bloodclart phone'
    dir_path = ''
    send(phone=phone_number, message=message, dir_path=dir_path)
    time.sleep(0.1)
    n -= 1
