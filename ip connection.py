import random
import time
import socket

#get current ip
ip = socket.gethostbyname(socket.gethostname())

print("Connecting to " + str(ip))
time.sleep(1)

#get how many times the 'code will run'
steps = int(random.random() * 10)

if steps < 1:
	print("Failed to send connect")
	exit()

print("Connected to " + str(ip))
print("Sending data")

words = ("0xFFFFFF", "0x0F0F0F", "0x0A012a", "0x16a82d", "0x013459")

time.sleep(1)

#'run the code'
while(steps > 0):
	text = ""
	multi = 10
	rand1 = int(random.random() * multi)
	rand2 = int(random.random() * multi)
	for i in range(0, rand1):
		#print a random amout of 'words' in a random order
		for j in range(0, int(rand2)):
			text = text + words[random.randint(0, len(words) - 1)] + " "

		rand2 = int(random.random() * multi)

		#print a random amount of spaces
		for k in range(0, int(rand2)):
			text = text + " "
	print(text + "\n")
	time.sleep(.5)
	steps = steps - 1

print("Done")