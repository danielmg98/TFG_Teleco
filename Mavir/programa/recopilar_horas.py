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
		char2 = original.read(1)
		if char2.isnumeric():
			char3 = original.read(3)
			time = char+char2+char3
			char4 = original.read(1)
			if char4 == ':':
				char5 = original.read(2)
				time = charhar2+char3+char4+char5
				nuevo.write(time+'\n')
			else:
				nuevo.write(time+'\n')
