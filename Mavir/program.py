import sys, os

if os.path.isfile('./Texto_nuevo/mavir02_new.txt'):
	os.remove('./Texto_nuevo/mavir02_new.txt')

if os.path.isfile('./Texto_nuevo/mavir02_new2.txt'):
	os.remove('./Texto_nuevo/mavir02_new2.txt')

if os.path.isfile('./Texto_nuevo/mavir02_new3.txt'):
	os.remove('./Texto_nuevo/mavir02_new3.txt')

if os.path.isfile('./Texto_nuevo/mavir02_new4.txt'):
	os.remove('./Texto_nuevo/mavir02_new4.txt')

if os.path.isfile('./Texto_nuevo/mavir02_new5.txt'):
	os.remove('./Texto_nuevo/mavir02_new5.txt')

if os.path.isfile('./Texto_nuevo/mavir02_new6.txt'):
	os.remove('./Texto_nuevo/mavir02_new6.txt')


def eliminar_especiales(original, nuevo):
	while 1:
		char = original.read(1)
		if not char:
			break
		if char == "/":
			pass
		elif char == "[":
			pass
		elif char == "]":
			pass
		elif char == "?":
			pass
		elif char == "¿":
			pass
		elif char == "¡":
			pass
		elif char == "!":
			pass
		elif char == "+":
			pass
		elif char == "-":
			pass
		elif char == "<":
			pass
		elif char == ">":
			pass
		elif char == "=":
			pass
		else:
			nuevo.write(char)

def eliminar_hhh(original, nuevo):
	while 1:
		char = original.read(1)
		if not char:
			break
		if char == 'h':
			char2 = original.read(1)
			if char2 == 'h':
				char3 = original.read(1)
				if char3 == 'h':
					pass
				else:
					nuevo.write(char2)
			else:
				nuevo.write(char)
				nuevo.write(char2)
		else:
			nuevo.write(char)

def eliminar_xxx(original, nuevo):
        while 1:
                char = original.read(1)
                if not char:
                        break
                if char == 'x':
                        char2 = original.read(1)
                        if char2 == 'x':
                                char3 = original.read(1)
                                if char3 == 'x':
                                        pass
                                else:
                                        nuevo.write(char2)
                        else:
                                nuevo.write(char)
                                nuevo.write(char2)
                else:
                        nuevo.write(char)

def eliminar_amp(original, nuevo):
	while 1:
		char = original.read(1)
		if not char:
			break
		if char =='&':
			char2 = original.read(1)
			if char2 == ' ':
				pass
			elif char2 == 'a' or 'e' or 'u' or 'm':
				char3 = original.read(1)
				if char3:
					pass
			else:
				pass
		else :
			nuevo.write(char)
			
		

def eliminar_comentarios(original, nuevo):
	while 1:
		char = original.read(1)
		if not char:
			break
		if char =='{':
			char2 = original.read(1)
			while char2 != '}':
				char2 = original.read(1)
			pass
		else:
			nuevo.write(char)	


def eliminar_nombres(original, nuevo):
	while 1:
		line = original.readline()
		if not line:
			break
		name = line[0:2]
		if name == 'ANS' or 'LRO' or 'JSL' or 'ENR' or 'IRA' or 'ANT' or 'ISI':
			newline = line[3:]
			nuevo.write(newline)
			pass
		else:
			nuevo.write(line)




mavir = open('./Texto_original/mavir02.txt','r')
mavir1 = open('./Texto_nuevo/mavir02_new.txt','w')

eliminar_especiales(mavir,mavir1)
	
mavir.close()
mavir1.close()

mavir = open('./Texto_nuevo/mavir02_new.txt','r')
mavir1 = open('./Texto_nuevo/mavir02_new2.txt','w')

eliminar_hhh(mavir,mavir1)

mavir.close()
mavir1.close()

mavir = open ('./Texto_nuevo/mavir02_new2.txt','r')
mavir1 = open('./Texto_nuevo/mavir02_new3.txt','w')

eliminar_xxx(mavir,mavir1)

mavir.close()
mavir1.close()


mavir = open('./Texto_nuevo/mavir02_new3.txt','r')
mavir1 = open('./Texto_nuevo/mavir02_new4.txt','w')

eliminar_amp(mavir,mavir1)

mavir.close()
mavir1.close()

mavir = open('./Texto_nuevo/mavir02_new4.txt','r')
mavir1 = open('./Texto_nuevo/mavir02_new5.txt','w')

eliminar_comentarios(mavir,mavir1)

mavir.close()
mavir1.close()


mavir = open('./Texto_nuevo/mavir02_new5.txt','r')
mavir1 = open('./Texto_nuevo/mavir02_new6.txt','w')

eliminar_nombres(mavir,mavir1)

mavir.close()
mavir1.close()




