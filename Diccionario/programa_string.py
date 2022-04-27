import sys, os

if os.path.isfile('./palabras_diccionario_new.txt'):
	os.remove('./palabras_lexicon_new.txt')

original = open('./palabras_diccionario.txt','rb')
nuevo = open('./palabras_diccionario_new.txt','w')


while 1:

	char = original.read()
	c = char.decode()
	if not char:
		break
	
	nuevo.write(c)

