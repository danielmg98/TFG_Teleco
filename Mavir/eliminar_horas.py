import sys, os

mavir = input('De que documento desea recortar las horas: ')

if os.path.isfile('./sin_horas'+mavir+'.txt'):
	os.remove('./sin_horas'+mavir+'.txt')

horas = open('./Horas/horas0'+mavir+'_new.txt','r')
lineas = open('./nuevo/mavir0'+mavir+'/mavir0'+mavir+'_new9.txt','r')
nuevo = open('./sin_horas'+mavir+'.txt','w')

hora = horas.readline()

while 1:

	line = lineas.readline()
	if not line:
		break
	if line[0].isnumeric():
		if line[1].isnumeric() or line[1] == ':':
			
			if line[0:] == hora[0:]:
				nuevo.write(line)
				hora = horas.readline()
	else:
	
		nuevo.write(line)	
