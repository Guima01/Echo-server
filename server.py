import socket
import threading

PORT = 4444
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
            if message == "quit":
                break
            elif message.startswith('echo '):
                message = message.split('echo ',1)
                if len(message) == 2:
                    message = message[1]
                    if message == '':
                        message = ' '
            print("Client message: ", message)
            self.csocket.send(bytes(message,'UTF-8'))

if __name__ == "__main__":

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((LOCALHOST, PORT))
    while True:
        s.listen()
        clientsock, clientAddress = s.accept()
        newthread = server(clientAddress, clientsock)
        newthread.start()
        
