import socket

SERVER = 'localhost'
PORT = 50007
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
message = "|| Connected ||"
client.sendall(bytes(message,'UTF-8'))
in_data =  client.recv(2048)
print("From Server: " ,in_data.decode())
while True:
  message = input()
  if message.startswith('echo '):
    message = message.split('echo ',1)
    if len(message) == 2:
      message = message[1]
      client.sendall(bytes(message,'UTF-8'))
      in_data =  client.recv(2048)
      print("From Server: " ,in_data.decode())
  if message == 'quit':
    client.sendall(bytes(message,'UTF-8'))
    break

client.close()
