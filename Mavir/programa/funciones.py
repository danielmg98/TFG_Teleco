import sys, os

def eliminar_archivos_existentes(i):
	if os.path.isfile('../nuevo/mavir0'+i+'/mavir0'+i+'_new.txt'):
		os.remove('../nuevo/mavir0'+i+'/mavir0'+i+'_new.txt')

	if os.path.isfile('../nuevo/mavir0'+i+'/mavir0'+i+'_new2.txt'):
		os.remove('../nuevo/mavir0'+i+'/mavir0'+i+'_new2.txt')

	if os.path.isfile('../nuevo/mavir0'+i+'/mavir0'+i+'_new3.txt'):
		os.remove('../nuevo/mavir0'+i+'/mavir0'+i+'_new3.txt')

	if os.path.isfile('../nuevo/mavir0'+i+'/mavir0'+i+'_new4.txt'):
		os.remove('../nuevo/mavir0'+i+'/mavir0'+i+'_new4.txt')

	if os.path.isfile('../nuevo/mavir0'+i+'/mavir0'+i+'_new5.txt'):
		os.remove('../nuevo/mavir0'+i+'/mavir0'+i+'_new5.txt')

	if os.path.isfile('../nuevo/mavir0'+i+'/mavir0'+i+'_new6.txt'):
		os.remove('../nuevo/mavir0'+i+'/mavir0'+i+'_new6.txt')

	if os.path.isfile('../nuevo/mavir0'+i+'/mavir0'+i+'_new7.txt'):
		os.remove('../nuevo/mavir0'+i+'/mavir0'+i+'_new7.txt')

	if os.path.isfile('../nuevo/mavir0'+i+'/mavir0'+i+'_new8.txt'):
		os.remove('../nuevo/mavir0'+i+'/mavir0'+i+'_new8.txt')

	if os.path.isfile('../nuevo/mavir0'+i+'/mavir0'+i+'_new9.txt'):
		os.remove('../nuevo/mavir0'+i+'/mavir0'+i+'_new9.txt')
	
	if os.path.isfile('../nuevo/mavir0'+i+'/mavir0'+i+'_new10.txt'):
		os.remove('../nuevo/mavir0'+i+'/mavir0'+i+'_new10.txt')

	if os.path.isfile('../nuevo/mavir0'+i+'/mavir0'+i+'_new11.txt'):
		os.remove('../nuevo/mavir0'+i+'/mavir0'+i+'_new11.txt')

	if os.path.isfile('../nuevo/mavir0'+i+'/mavir0'+i+'_new12.txt'):
		os.remove('../nuevo/mavir0'+i+'/mavir0'+i+'_new12.txt')

	if os.path.isfile('../nuevo/mavir0'+i+'/mavir0'+i+'_new13.txt'):
		os.remove('../nuevo/mavir0'+i+'/mavir0'+i+'_new13.txt')

	if os.path.isfile('../nuevo/htk/mavir0'+i+'_htk.txt'):
		os.remove('../nuevo/htk/mavir0'+i+'_htk.txt')

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
		elif char == ".":
			pass
		elif char == "#":
			pass
		elif char == "¬":
			pass
		else:
			nuevo.write(char)

def eliminar_letras(original, nuevo, letra):
	while 1:
		char = original.read(1)
		if not char:
			break
		if char == letra:
			char2 = original.read(1)
			if char2 == letra:
				char3 = original.read(1)
				if char3 == letra:
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
			while char2 != ' ':
				char2 = original.read(1)
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

def eliminar_espacios(original, nuevo):
	while 1:
		char = original.read(1)
		if not char:
			break
		if char == ' ':
			nuevo.write(char)
			char2 = original.read(1)
			while char2 == ' ':
				char2 = original.read(1)
				pass
			nuevo.write(char2)
		else:
			nuevo.write(char)

def eliminar_espacios_inicio(original, nuevo):
	while 1:
		line = original.readline()
		if not line:
			break
		if line[0] == ' ':
			newline = line[1:]
			nuevo.write(newline)
		else:
			nuevo.write(line)

def cambiar_espacios_lineas(original, nuevo):
	while 1:
		char = original.read(1)
		if not char:
			break
		if char == ' ':
			nuevo.write('\n')
		else:
			nuevo.write(char)

def eliminar_horas(original,nuevo,horas):

	hora = horas.readline()

	while 1:

		line = original.readline()
		if not line:
			break
		if line[0].isnumeric():
			if line[1].isnumeric() or line[1] == ':':
				if line[0:] == hora[0:]:
					nuevo.write(line)
					hora = horas.readline()
		else:
	
			nuevo.write(line)


def cambiar_horas_puntos(original,nuevo):
	while 1:
		line = original.readline()
		if not line:
			break
		if line[0].isnumeric():
			if line[1].isnumeric() or line[1] == ':':
				if line[2].isnumeric() or line[2] == ':':
					nuevo.write('.\n')
				else:
					nuevo.write(line)
			else:
				nuevo.write(line)
		else:
			nuevo.write(line)


def formato_htk(original,nuevo,i):

	nuevo.write('#!MLF!#\n')
	nuevo.write('"*/mavir0'+i+'_1.lab"\n')
	j = 2

	while 1:
		line = original.readline()
		if not line:
			break
		if line[0] == '.':
			nuevo.write(line)
			nuevo.write('"*/mavir0'+i+'_'+str(j)+'.lab"\n')
			j = j+1
		else:
			nuevo.write(line)
	
		
def cambiar_minusculas(original,nuevo):

	while 1:
		char = original.read(1)

		if not char:
			break

		if char == 'A':
			nuevo.write('a')

		elif char == 'B':
			nuevo.write('b')

		elif char == 'C':
			nuevo.write('c')

		elif char == 'D':
			nuevo.write('d')

		elif char == 'E':
			nuevo.write('e')

		elif char == 'F':
			nuevo.write('f')

		elif char == 'G':
			nuevo.write('g')

		elif char == 'H':
			nuevo.write('h')

		elif char == 'I':
			nuevo.write('i')

		elif char == 'J':
			nuevo.write('j')

		elif char == 'K':
			nuevo.write('k')

		elif char == 'L':
			nuevo.write('l')

		elif char == 'M':
			nuevo.write('m')

		elif char == 'N':
			nuevo.write('n')

		elif char == 'Ñ':
			nuevo.write('ñ')

		elif char == 'O':
			nuevo.write('o')

		elif char == 'P':
			nuevo.write('p')

		elif char == 'Q':
			nuevo.write('q')

		elif char == 'R':
			nuevo.write('r')

		elif char == 'S':
			nuevo.write('s')

		elif char == 'T':
			nuevo.write('t')

		elif char == 'U':
			nuevo.write('u')

		elif char == 'V':
			nuevo.write('v')

		elif char == 'W':
			nuevo.write('w')

		elif char == 'X':
			nuevo.write('x')

		elif char == 'Y':
			nuevo.write('y')

		elif char == 'Z':
			nuevo.write('z')

		else:
			nuevo.write(char)





