import time
from socket import *
                    
host = "127.0.0.1"# FILL IN START		# FILL IN END
port = 12000# FILL IN START		# FILL IN END
timeout = 1 # in seconds
	
serverName = 'hostname'

clientSocket = socket(AF_INET, SOCK_DGRAM)

clientSocket.settimeout(timeout)

ptime = 0  

while ptime < 10: 
	ptime += 1
	message = 'Ping: ' + str(ptime)# FILL IN START		# FILL IN END
    
	addr = (host, port)
	
	start = time.time()
	clientSocket.sendto(message, addr)
	
	try:
		data, server = clientSocket.recvfrom(1024)
		end = time.time()
		elapsed = end - start
		print 'Data' + str(data) + ', RTT: ' + str(elapsed)
		
	except:
		print "Request timed out."
		continue

clientSocket.close()
 
