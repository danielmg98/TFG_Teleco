import sys, os
import funciones_hora as f


mavir = input('Las horas de que documento desea reducir: ')

if os.path.isfile('./nuevas/horas0'+mavir+'_new.txt'):
	os.remove('./nuevas/horas0'+mavir+'_new.txt')

horas = open('./antiguas/horas0'+mavir+'.txt','r')
horas2 = open('./antiguas/horas0'+mavir+'.txt','r')
nuevo = open('./nuevas/horas0'+mavir+'_new.txt','w')

line = horas.readline()
line2 = horas2.readline()
time = line[0:-1]
nuevo.write(time+'\n')
dif_sec = 0

while 1:

	nextline = horas2.readline()
	if not nextline:
		break
	time2 = nextline[0:-1]
	dif_sec = f.diferencia_segundos(time,time2)
	if int(dif_sec) >= 4:
		nuevo.write(time2+'\n')
	
	line = horas.readline()
	time = line[0:-1]
	

horas.close()
horas2.close()
nuevo.close()
