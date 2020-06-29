import socket
ip = input('Enter ip Target\n')
port = int(input('Enter Port Target\n'))
with socket.socket() as my_socket:
	my_socket.connect((ip, port))
	print('Okay Connected target \U0001f44f')
	while True:
		print(my_socket.recv(126).decode(), file=open('log.txt', 'a', encoding='UTF-8'))