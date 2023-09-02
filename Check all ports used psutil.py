#pip install psutil 
import psutil

#get object
proc = psutil.Process(pid)

# Check all ports used by a specific pid:
print (proc.connections())

# Check all ports used on the local machine:
print (psutil.net_connections())
