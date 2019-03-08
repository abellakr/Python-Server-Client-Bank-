import socket
import sys
import select

# im using sys.stdout.write to print messages because the print() method 
# automatically replaces every space to \n in every incoming server message

# address variable
HOST = 'eagle.cs.umanitoba.ca' # currently bounded to a well-known address in the uofm unix network
PORT = 13244
data = ""
clientExited = 0

# create socket connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
socket_list = [sys.stdin, s]

# socket loop
while clientExited != 1: #boolean will break if user types in 'e'
    read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

    for sock in read_sockets:
        # recieve message
        if sock == s:
            # reecieve message from server
            data = sock.recv(1024)
            # make sure data is valid, if not disconnect
            if not data:
                print('\nDisconnected from server')
                sys.exit()
            # else, decode and print to client
            else:
                message = data.decode() 
                sys.stdout.write(message) #write message to client 
                sys.stdout.flush() #flushing out the system standard out buffer
        # send message
        else:
            # read from standard input then send to client
            msg = sys.stdin.readline() 
            # client exit command triggered, end socket loop
            if msg.strip() == 'e':
                clientExited = 1 
            else:
                s.send(bytes(msg))
                sys.stdout.flush() #flushing out the system standard out buffer

print("closing socket")
s.close()
