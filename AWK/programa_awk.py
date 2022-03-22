import sys, os
import funciones_awk as f

if os.path.isfile('./awk_mavir02.txt'):
	os.remove('./awk_mavir02.txt')

horas1 = open('./horas_mavir02.txt','r')
horas2 = open('./horas_mavir02.txt','r')
nuevo = open('./awk_mavir02.txt','w')

f.calcular_duracion(horas1,horas2,nuevo)

horas1.close()
horas2.close()
nuevo.close()
	


