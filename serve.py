"""
serve.py

Instantiates a socket-adventure `Server` and serves it on a specified
port.

You should not need to make any changes in this file.
"""


import sys

from server import Server # imports server class

try:
    port = int(sys.argv[1]) # gets port number from command line
except IndexError:
    print("Please include a port number, eg: python serve.py 50000")
    exit(-1)

server = Server(port) # creates instance of server class
server.serve() # invokes that instances serve method

