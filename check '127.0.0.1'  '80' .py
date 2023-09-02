import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#2 Second Timeout
sock.settimeout(2)   

result = sock.connect_ex(('127.0.0.1',80))

if result == 0:
  print 'port OPEN'
else:
  print 'port CLOSED, connect_ex returned: '+str(result)
