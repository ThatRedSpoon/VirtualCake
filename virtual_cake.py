import sys
import socket
import math
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('10.0.21.32', 3000)

print "Starting Server on %s:%s" % server_address

sock.bind(server_address)

sock.listen(10)
while True:
    print "Waiting for connections!"
    connection, client_address = sock.accept()
    try:
        data = connection.recv(16)
        print "Connection From " +  client_address[0] + ":" + str(client_address[1])
        if data == "giveinfo":
            connection.send("answer")
    finally:
        connection.close()



