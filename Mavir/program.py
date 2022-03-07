import sys, os

#if './Texto_nuevo/mavir02_new.txt' != None:
#	os.remove('./Texto_nuevo/mavir02_new.txt')

mavir = open('./Texto_original/mavir02.txt','r')
mavir1 = open('./Texto_nuevo/mavir02_new.txt','w')

while 1:
	char = mavir.read(1)
	if not char:
		break
	if char == "/":
		pass
	elif char == "[":
		pass
	elif char == "]":
		pass
	else:
		mavir1.write(char)
	
mavir.close()
mavir1.close()



