import socket


target_host = "www.google.pl"
target_port = 80

#socket client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connection
client.connect((target_host, target_port))

#data send
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n ")

#data receive

response = client.recv(4096)

print response
