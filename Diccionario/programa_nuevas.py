import sys, os

original = open('palabras_nuevas.txt','r')
nuevo = open('palabras_diferentes.txt','w')

while 1:

	line = original.readline()
	if not line:
		break
	if line[0] == '>' or line[0] == '<':
		newline = line[2:]		
		nuevo.write(newline)
	else:
		pass

