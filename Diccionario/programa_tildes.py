import sys, os

'''
if os.path.isfile('./palabras_lexicon_new.txt'):
	os.remove('./palabras_lexicon_new.txt')
'''

original = open('./diccionario_con_tildes.txt','r')
nuevo = open('./diccionario_definitivo.txt','w')

while 1:

	char = original.read(1)
	if not char:
		break
	
	if char == 'á':
		nuevo.write('a')

	elif char == 'é':
		nuevo.write('e')

	elif char == 'í':
		nuevo.write('i')

	elif char == 'ó':
		nuevo.write('o')

	elif char == 'ú':
		nuevo.write('u')
	else:
		nuevo.write(char)
