import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('172.18.0.3', 3000))

client.send("giveinfo")

response = client.recv(4096)
print response