import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)

print "( Y ) listening on %s : %d " % (bind_ip, bind_port)


# client handler method
def handle_client(client_socket):
    request = client_socket.recv(1024)
    print "( Y ) Receiver: %s" % request
    client_socket.send("( * Y * )")
    client_socket.close()


while True:
    client, addr = server.accept()
    print "( * Y * ) Accepted connection from teh : %s:%d " % (addr[0], addr[1])
    # client handler create n star mooooooon!!!!!!!!
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
