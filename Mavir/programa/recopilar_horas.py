import sys, os

if os.path.isfile('./copia02.txt'):
	os.remove('./copia02.txt')

original = open('../nuevo/mavir02_new6.txt','r')

nuevo = open('./copia02.txt','w')

while 1:
	char = original.read(1)
	if not char:
		break
	if char.isnumeric():
		time = char
		char2 = original.read(1)
		if char2.isnumeric():
			time = char + char2
			char3 = original.read(1)
			if char3 == ':':
				time = char + char2 + char3
				char4= original.read(1)
				if char4.isnumeric():
					time = char + char2 + char3 +char4
					char5 = original.read(1)
					if char5.isnumeric():
						time = char + char2+ char3 + char4 +char5
						nuevo.write(time+'\n')
		elif char2 == ':':
			time = char + char2
			char3 = original.read(5)
			time = time + char3
			nuevo.write(time+'\n')
		else:
			pass



original.close()

nuevo.close()

