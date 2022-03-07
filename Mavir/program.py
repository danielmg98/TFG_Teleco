import sys, os

if os.path.isfile('./Texto_nuevo/mavir02_new.txt'):
	os.remove('./Texto_nuevo/mavir02_new.txt')

if os.path.isfile('./Texto_nuevo/mavir02_new2.txt'):
	os.remove('./Texto_nuevo/mavir02_new2.txt')

if os.path.isfile('./Texto_nuevo/mavir02_new3.txt'):
	os.remove('./Texto_nuevo/mavir02_new3.txt')

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
