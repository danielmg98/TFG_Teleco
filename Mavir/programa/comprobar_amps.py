import os, sys

original = open('../nuevo/mavir02_new3.txt','r')
nuevo = open('./recopilacion.txt','w')

while 1:
	
	char = original.read(1)
	if not char:
		break
	if char == '&':
		nuevo.write(char)
		char2 = original.read(1)
		while char2 != ' ':
			nuevo.write(char2)
			char2 = original.read(1)
		nuevo.write('\n')


