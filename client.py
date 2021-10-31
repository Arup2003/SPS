import socket, threading

c = socket.socket()



c.connect(("13.127.247.216", 14572))
print("CONNECTED")

name = input("NAME")
yay = 0
asking = "yes"
def choice():
	global asking
	if asking == "yes":
		global name
		c.send(bytes(name,'utf-8'))
		print("SENT")
		answer = c.recv(1024).decode()
		return answer
		asking = "no"
	if asking == "no":
		print("")


while True:
	data = threading.Thread(target = choice).start()
	if data == True:
		print("okay")
	else:
		print(data)






