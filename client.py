import socket

SERVER = 'localhost'
PORT = 4444
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
message = "|| Connected ||"
client.sendall(bytes(message,'UTF-8'))
in_data =  client.recv(2048)
print("From Server: " ,in_data.decode())
while True:
  message = input()
  if message == 'quit':
    client.sendall(bytes(message,'UTF-8'))
    break
  elif message.startswith('echo '):
    client.sendall(bytes(message,'UTF-8'))
    in_data =  client.recv(2048)
    print("From Server: " ,in_data.decode())


client.close()
