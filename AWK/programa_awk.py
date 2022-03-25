import sys, os
import funciones_awk as f

mavir=input('Que documento desea convertir: ')

if os.path.isfile('./AWKs/awk_mavir0'+mavir+'.txt'):
	os.remove('./AWKs/awk_mavir0'+mavir+'.txt')

horas1 = open('./Horas/horas0'+mavir+'_new.txt','r')
horas2 = open('./Horas/horas0'+mavir+'_new.txt','r')
nuevo = open('./AWKs/awk_mavir0'+mavir+'.txt','w')

f.calcular_duracion(horas1,horas2,nuevo,mavir)

horas1.close()
horas2.close()
nuevo.close()
	


