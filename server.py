import socket
import threading

PORT = 50007
LOCALHOST = 'localhost'

class server(threading.Thread):
    def __init__(self,clientAddress,clientSocket):
        threading.Thread.__init__(self)
        self.csocket = clientSocket
        print("New connection")
    def run(self):
        message = ''
        while True:
            data = self.csocket.recv(2048)
            message = data.decode()
            print("Client message ", message)
            if message == "quit":
                break
            self.csocket.send(bytes(message,'UTF-8'))

if __name__ == "__main__":

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((LOCALHOST, PORT))
    while True:
        s.listen()
        clientsock, clientAddress = s.accept()
        newthread = server(clientAddress, clientsock)
        newthread.start()
        
