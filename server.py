
import socket
import time
import sys
import os
import re

# define machine 
HOST = socket.gethostname()
# assigned port in cs.umanitoba.ca
PORT = 13244

#create bank dict
bank = {}

# create socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# try bind, must catch
try:
    serverSocket.bind(('', PORT))
except Exception:
    print("Error connecting to HOST and PORT.")

print("Welcome to Karlos' banking system")

# single client for now
print ("Listening for requests...\n")
serverSocket.listen(socket.SOMAXCONN)
clientSocket , newAddress = serverSocket.accept()
print ("{c} connected to our server\n").format(c=newAddress)

while(1):
    request = bytes.decode(clientSocket.recv(1024))
    tokens = re.split('<|,|>', request)
    print(request)

    if tokens[0] == 'c':
        bank[tokens[1]] = 0
        clientSocket.send("Created new client "+tokens[1]+" with balance of 0\n")
    
    if tokens[0] == 'r':
        if tokens[1] in bank:
            clientSocket.send("Client "+tokens[1]+" has a balance of "+str(bank.get(tokens[1]))+"\n")
        else:
            clientSocket.send("Client "+tokens[1]+" does not exist!\n")

    if tokens[0] == 'd':
        if tokens[1] in bank: 
            oldBalance = bank.get(tokens[1])
            newBalance = int(oldBalance) + int(tokens[2])
            update = {tokens[1]: newBalance}
            bank.update(update)
            clientSocket.send("Client "+tokens[1]+"'s new balance is "+str(newBalance)+"\n")
        else:
            clientSocket.send("Client "+tokens[1]+" does not exist!\n")

    if tokens[0] == 'w':
        if tokens[1] in bank: 
            oldBalance = bank.get(tokens[1])
            newBalance = int(oldBalance) - int(tokens[2])
            update = {tokens[1]: newBalance}
            bank.update(update)
            clientSocket.send("Client "+tokens[1]+"'s new balance is "+str(newBalance)+"\n")
        else:
            clientSocket.send("Client "+tokens[1]+" does not exist!\n")



            