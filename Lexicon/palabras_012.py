import sys, os

original = open('palabras_nuevas_012.txt','r')
nuevo = open('palabras_unicas_012.txt','w')

while 1:

	line = original.readline()
	if not line:
		break
	if line[0] == '>':
		newline = line[2:]
		nuevo.write(newline)
