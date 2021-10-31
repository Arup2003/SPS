import socket

s = socket.socket()

s.bind(("localhost", 9999))

print("Started server")

s.listen(3)
print('waiting')
c1, addr = s.accept()
print("1 Connected")
c2, addr1 = s.accept()
print("BOTH CONNECTED!")

while True:
	
	player1 = c1.recv(1024).decode()
	player2 = c2.recv(1024).decode()

	c1_send = player2 + "w"
	c2_send = player1 + "l"
	c1__send = player2 + "l"
	c2__send = player1 +"w"
	c1___send = player2 + "t"
	c2___send = player1 + "t"

	if player1 == "A" and player2 == "B" or player1 == "B" and player2 == "C" or player1 == "C" and player2 == "A":
		c1.send(bytes(c1__send, "utf-8"))
		c2.send(bytes(c2__send, "utf-8"))
		print("SENT RESULTS")

	elif player1 == "A" and player2 == "C" or player1 == "B" and player2 == "A" or player1 == "C" and player2 == "B":
		c1.send(bytes(c1_send, "utf-8"))
		c2.send(bytes(c2_send, "utf-8"))
		print("SENT RESULTS")

	elif player1 == "A" and player2 == "A" or player1 == "B" and player2 == "B" or player1 == "C" and player2 == "C":
		c1.send(bytes(c1___send, "utf-8"))
		c2.send(bytes(c2___send, "utf-8"))
		print("SENT RESULTS")


