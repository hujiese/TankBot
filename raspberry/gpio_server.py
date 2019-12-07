#!/usr/bin/python3

import socket
import RPi.GPIO as GPIO

pin1 = 23
pin2 = 18
pin3 = 25
pin4 = 24

pin5 = 17
pin6 = 27

currentDirection = 'S'
currentPortDrition = 'T'
address='192.168.12.1'     #监听哪些网络  127.0.0.1是监听本机 0.0.0.0是监听整个网络
port=8040             #监听自己的哪个端口
buffsize=1024          #接收从客户端发来的数据的缓存区大小

def forward():
    GPIO.output(pin1, GPIO.HIGH)
    GPIO.output(pin2, GPIO.LOW)
    GPIO.output(pin3, GPIO.HIGH)
    GPIO.output(pin4, GPIO.LOW)
    
def back():
    GPIO.output(pin1, GPIO.LOW)
    GPIO.output(pin2, GPIO.HIGH)
    GPIO.output(pin3, GPIO.LOW)
    GPIO.output(pin4, GPIO.HIGH)

def stop():
    GPIO.output(pin1, GPIO.LOW)
    GPIO.output(pin2, GPIO.LOW)
    GPIO.output(pin3, GPIO.LOW)
    GPIO.output(pin4, GPIO.LOW)

def turn_left():
    GPIO.output(pin1, GPIO.LOW)
    GPIO.output(pin2, GPIO.HIGH)
    GPIO.output(pin3, GPIO.HIGH)
    GPIO.output(pin4, GPIO.LOW)
    
def turn_right():
    GPIO.output(pin1, GPIO.HIGH)
    GPIO.output(pin2, GPIO.LOW)
    GPIO.output(pin3, GPIO.LOW)
    GPIO.output(pin4, GPIO.HIGH)
    
def port_left():
    GPIO.output(pin5, GPIO.LOW)
    GPIO.output(pin6, GPIO.HIGH)
	
def port_right():
    GPIO.output(pin5, GPIO.HIGH)
    GPIO.output(pin6, GPIO.LOW)

def port_stop():
    GPIO.output(pin5, GPIO.LOW)
    GPIO.output(pin6, GPIO.LOW)
	
def main():
    global currentDirection
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin1, GPIO.OUT)
    GPIO.setup(pin2, GPIO.OUT)
    GPIO.setup(pin3, GPIO.OUT)
    GPIO.setup(pin4, GPIO.OUT)
    GPIO.setup(pin5, GPIO.OUT)
    GPIO.setup(pin6, GPIO.OUT)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    s.setsockopt(socket.SOL_TCP, socket.TCP_KEEPIDLE, 2)
    s.setsockopt(socket.SOL_TCP, socket.TCP_KEEPINTVL, 1)
    s.setsockopt(socket.SOL_TCP, socket.TCP_KEEPCNT, 3)
    s.bind((address,port))
    s.listen(1)     #最大连接数
    while True:
        clientsock,clientaddress=s.accept()
        print('connect from:',clientaddress)
    #传输数据都利用clientsock，和s无关
        while True: 
            try:
                 recvdata=clientsock.recv(buffsize).decode('utf-8')
            except Exception as e:
                 print('Time out ...')
            if not recvdata:
                print('client off line ...')
                break
            if recvdata[0]=='l':
                # add the port left code
                currentPortDrition = 'l'
                print('port left ...')
                port_left()
            if recvdata[0]=='r':
                # add the port right code
                currentPortDrition = 'r'
                print('port right ...')
                port_right()
            if recvdata[0]=='T':
                # add the port right code
                currentPortDrition = 'T'
                print('port stop ...')
                port_stop()
            if recvdata[0]=='F':
                # add the move forward code
                currentDirection = 'F'
                print('move forword ...')
                forward()
            if recvdata[0]=='B':
                # add the move back code
                currentDirection = 'B'
                print('move back ...')
                back()
            if recvdata[0]=='L':
                # add the move left code
                print('move left ...')
                turn_left()
            if recvdata[0]=='R':
                # add the move right code
                print('move right ...')
                turn_right()
            if recvdata[0]=='X':
                if currentDirection == 'F':
                    print('move forword ...')
                    forward()
                   # add the move forward code
                if currentDirection == 'B':
                    print('move back ...')
                    back()
                   # add the move back code
                if currentDirection == 'S':
                    print('move stop ...')
                    stop()
                   # add the move stop code
            if recvdata[0]=='S':
                # add the move stop code
                currentDirection = 'S'
                print('move stop ...')
                stop()
        clientsock.close()
    s.close()

if __name__ == "__main__":
    main()
    
