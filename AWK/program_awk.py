import sys, os

if os.path.isfile('./awk_mavir02.txt'):
	os.remove('./awk_mavir02.txt')

def escribir_labels_horas():

	htk = open('./mavir02_htk.txt','r')
	horas = open('./horas_mavir02.txt','r')
	nuevo = open('./awk_mavir02.txt','w')

	while(1):
	
		line = htk.readline()
		if not line:
			break
		if line[0] == '*':
			time = horas.readline()
			if not time:
				break
			nuevo.write(line)
			nuevo.write(time)
	
	htk.close()
	horas.close()
	nuevo.close()

#escribir_labels_horas()

def calcular_duracion():
	
	horas = open('./horas_mavir02.txt','r')
	nuevo = open('./awk_mavir02.txt','w')
	
	while 1:
		
		line = horas.readline()
		if not line:
			break
		i=0
		for c in line:
			if c == '\n':
				time = line[0:i]
				line2 = horas.readline()
				j=0
				for x in line2:
					if x == '\n':
						time2 = line2[0:j]
					j=j+1
				
				nuevo.write('Desde '+time+' hasta '+time2+'\n')
			i = i+1 
	
	horas.close()
	nuevo.close()
	
calcular_duracion()




























