from time import sleep
import socket, ipaddress, threading

# Here's a fast multi-threaded port scanner:

max_threads = 50
final = {}
def check_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
        #sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        socket.setdefaulttimeout(2.0) # seconds (float)
        result = sock.connect_ex((ip,port))
        if result == 0:
            # print ("Port is open")
            final[ip] = "OPEN"
        else:
            # print ("Port is closed/filtered")
            final[ip] = "CLOSED"
        sock.close()
    except:
        final[ip] = "EXCEPTION"
        
port = 22
for ip in ipaddress.IPv4Network('95.217.210.0/24'): 
    threading.Thread(target=check_port, args=[str(ip), port]).start()
    #sleep(0.1)

    # limit the number of threads.
    while threading.active_count() > max_threads :
        sleep(1)


sorted_ips = dict(sorted(final.items(), key=lambda item: tuple(map(int, item[0].split('.')))))

for ip, state in sorted_ips.items():
    print(ip, state)
