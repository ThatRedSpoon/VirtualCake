import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('https://cakething.herokuapp.com', 3000))

client.send("giveinfo")

response = client.recv(4096)
print response
