#!/usr/bin/python3

import sys
import socket
import ipaddress
import subprocess

print('')
print('Simple TCP/IP Port Scanner')
print('')

ipAddress = input("IPv4 Address: ")
port = int(input("TCP/UDP Port: "))

print('')
str(ipAddress)
print('')

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ipAddress, port))
    if result == 0:
        print(f"Port {port} Open")
        break
    elif result != 0:
        print(f"Port {port} Closed")
        break

