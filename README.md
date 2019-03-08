# Server/Client socket network implemented in Python.

## the app consists of a bank stored in the server and a client can connect to communicate with the server with the use of sockets and be able to access the bank and its features.

## how to compile
terminal command:

python server.py

python client.py

## command syntax
c<[acctid]>  - creates a new account
r<[acctid]> - retrieves an existing account
d<[amount],[acctid]> - deposits the amount into the given account 
w<[amount],[acctid]> - withdraws the amount from the given account 

