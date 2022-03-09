import sys, os

if os.path.isfile('./copia02.txt'):
	os.remove('./copia02.txt')

original = open('../nuevo/mavir02_new6.txt','r')
nuevo = open('./copia02.txt','w')

def recopilar_hora(original,nuevo):

	while 1:
		char = original.read(1)
		if not char:
			break
		if char.isnumeric():
			time = char
			char2 = original.read(1)
			if char2.isnumeric():
				time = time + char2
				char3 = original.read(1)
				if char3 == ':':
					time = time + char3
					char4= original.read(1)
					if char4.isnumeric():
						time = time+char4
						char5 = original.read(1)
						if char5.isnumeric():
							time = time +char5
							char6 = original.read(1)
							if char6 == ':':
								char7 = original.read(1)
								char8 = original.read(1)
								time = time + char7 + char8
								nuevo.write(time+'\n')
							else:
								nuevo.write(time+'\n')


recopilar_hora(original,nuevo)

original.close()
nuevo.close()
