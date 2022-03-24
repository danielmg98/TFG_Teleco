import sys, os
import funciones_awk as f

'''
if os.path.isfile('./AWKs/awk_mavir02.txt'):
	os.remove('./AWKs/awk_mavir02.txt')

if os.path.isfile('./AWKs/awk_mavir03.txt'):
	os.remove('./AWKs/awk_mavir03.txt')

if os.path.isfile('./AWKs/awk_mavir04.txt'):
	os.remove('./AWKs/awk_mavir04.txt')

if os.path.isfile('./AWKs/awk_mavir06.txt'):
	os.remove('./AWKs/awk_mavir06.txt')

if os.path.isfile('./AWKs/awk_mavir07.txt'):
	os.remove('./AWKs/awk_mavir07.txt')

if os.path.isfile('./AWKs/awk_mavir09.txt'):
	os.remove('./AWKs/awk_mavir09.txt')

if os.path.isfile('./AWKs/awk_mavir011.txt'):
	os.remove('./AWKs/awk_mavir011.txt')

if os.path.isfile('./AWKs/awk_mavir013.txt'):
	os.remove('./AWKs/awk_mavir013.txt')

if os.path.isfile('./AWKs/awk_mavir08.txt'):
	os.remove('./AWKs/awk_mavir08.txt')
'''

mavir=input('Que documento desea convertir: ')

horas1 = open('./Horas/horas0'+mavir+'.txt','r')
horas2 = open('./Horas/horas0'+mavir+'.txt','r')
nuevo = open('./AWKs/awk_mavir0'+mavir+'.txt','w')

f.calcular_duracion(horas1,horas2,nuevo,mavir)

horas1.close()
horas2.close()
nuevo.close()
	


