import sys, os
import funciones_hora as f


mavir = input('Las horas de que documento desea reducir: ')

if os.path.isfile('./nuevas/horas0'+mavir+'_new.txt'):
	os.remove('./nuevas/horas0'+mavir+'_new.txt')

horas = open('./antiguas/horas0'+mavir+'.txt','r')
horas2 = open('./antiguas/horas0'+mavir+'.txt','r')
nuevo = open('./nuevas/horas0'+mavir+'_new.txt','w')

line = horas.readline()
nuevo.write(line)
nextline = horas2.readline()
dif_sec = 0

while 1:

	if not line:
		break
	i=0
	for c in line:
		if c == '\n':
			time = line[0:i]
			nextline = horas2.readline()
			j=0
			for x in nextline:
				if x == '\n':
					time2 = nextline[0:j]
					j=j+1
	
	dif_sec = f.diferencia_segundos(time,time2)
	
	
	if dif_sec >= 4:
		nuevo.write(nextline)
	
	line = horas.readline()
	nextline = horas2.readline()

horas.close()
horas2.close()
nuevo.close()
