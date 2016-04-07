from socket import *

# Message to send
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Our mail server is smtp.stud.ntnu.no
mailserver = 'smtp.stud.ntnu.no'

# Create socket called clientSocket and establish a TCP connection 
# (use the appropriate port) with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientPort = 6789
clientSocket.connect((mailserver, clientPort))
#Fill in end

recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
	print '220 reply not received from server.'

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server.'

# Send MAIL FROM command and print server response.
# Fill in start
fromCommand = 'MAIL FROM H-kon\r\n'
clientSocket.send(fromCommand)
recv2 = clientSocket.recv(1024)
print recv2
if recv2[:3] != '250':
	print '250 reply not received from server.'
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
rcptCommand = 'RCPT Alice\r\n'
clientSocket.send(rcptCommand)
recv3 = clientSocket.recv(1024)
print recv3
if recv3[:3] != '250':
	print '250 reply not received from server.'
# Fill in end

# Send DATA command and print server response.
# Fill in start
dataCommand = 'DATA\r\n'
clientSocket.send(heloCommand)
recv4 = clientSocket.recv(1024)
print recv4
if recv4[:3] != '250':
	print '250 reply not received from server.'
# Fill in end

# Send message data.
# Fill in start
msgCommand = 'Yo Alice\r\n'
clientSocket.send(msgCommand)
recv5 = clientSocket.recv(1024)
print recv5
if recv5[:3] != '250':
	print '250 reply not received from server.'
# Fill in end

# Message ends with a single period.
# Fill in start
periodCommand = '.\r\n'
clientSocket.send(periodCommand)
recv6 = clientSocket.recv(1024)
print recv6
if recv6[:3] != '250':
	print '250 reply not received from server.'
# Fill in end

# Send QUIT command and get server response.
# Fill in start
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand)
recv7 = clientSocket.recv(1024)
print recv7
if recv7[:3] != '250':
	print '250 reply not received from server.'
# Fill in end