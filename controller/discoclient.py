# 04/06/19

import socket
import os

os.chdir(r'/home/pi/Desktop/cabot/cabot-discoball')

s = socket.socket()

# host and port of caBot
host = '192.168.x.x'
port = 12345

# connect to caBot
s.connect((host,port))
while True:   
    test = s.recv(1024).decode('ascii')
    print(test)
    
    if test == 'partyTime':
        os.system('sudo ./light')
