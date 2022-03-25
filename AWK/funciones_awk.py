import sys, os


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

def diferencia_segundos(inicio,fin,nuevo):
	
	if len(inicio) == 5:

		inicio_min = int(inicio[0:2])
		inicio_sec = int(inicio[3:5])
	

	if len(fin) == 5:
		
		fin_min = int(fin[0:2])
		fin_sec = int(fin[3:5])

	if len(inicio) == 7:

		inicio_min = int(inicio[2:4])
		inicio_sec = int(inicio[5:7])
		inicio_hora = int(inicio[0])
	

	if len(fin) == 7:
		
		fin_min = int(fin[2:4])
		fin_sec = int(fin[5:7])
		fin_hora = int(fin[0])

	if len(fin)== 5 and len(inicio) == 5:

		if fin_min == inicio_min:
			dif_sec = fin_sec - inicio_sec

		if fin_min >= inicio_min and fin_sec >= inicio_sec:
			dif_min = fin_min - inicio_min
			dif_sec = (fin_sec - inicio_sec) + 60*dif_min

		if fin_min >= inicio_min and fin_sec < inicio_sec:
			dif_min = fin_min - inicio_min
			dif_sec = (60-inicio_sec)+fin_sec+60*(dif_min-1)
	
	if len(fin) == 7 and len(inicio) == 7:
	
		if fin_hora == inicio_hora:
						
			if fin_min == inicio_min:
				dif_sec = fin_sec - inicio_sec

			if fin_min > inicio_min and fin_sec >= inicio_sec:
				dif_min = fin_min - inicio_min
				dif_sec = (fin_sec - inicio_sec) + 60*dif_min

			if fin_min > inicio_min and fin_sec < inicio_sec:
				dif_min = fin_min - inicio_min
				dif_sec = (60 - inicio_sec) + fin_sec + 60*(dif_min-1)
		if fin_hora > inicio_hora:
	
			dif_hora = fin_hora - inicio_hora
			
			if fin_min == inicio_min:
				dif_sec = fin_sec - inicio_sec+3600*dif_hora

			if fin_min > inicio_min and fin_sec >= inicio_sec:
				dif_min = fin_min - inicio_min
				dif_sec = (fin_sec - inicio_sec) + 60*dif_min + 3600* dif_hora

			if fin_min > inicio_min and fin_sec < inicio_sec:
				dif_min = fin_min - inicio_min
				dif_sec = (60 - inicio_sec) + fin_sec + 60*(dif_min-1) + 3600*dif_hora

			if inicio_min > fin_min and fin_sec > inicio_sec:
				dif_min = (60-inicio_min)+fin_min + 3600*(fin_hora-1)
				dif_sec = fin_sec - inicio_sec + 60*dif_min			
			if inicio_min > fin_min and inicio_sec > fin_sec:
				
				dif_min = 60-inicio_min+fin_min+3600*(fin_hora-1)
				dif_sec = 60-inicio_sec+fin_sec+60*(dif_min-1)			
			
	if len(fin)>len(inicio):

		inicio_hora = 0

		dif_hora = fin_hora - inicio_hora
			
		if fin_min == inicio_min:
			dif_sec = fin_sec - inicio_sec+3600*dif_hora

		if fin_min > inicio_min and fin_sec >= inicio_sec:
			dif_min = fin_min - inicio_min
			dif_sec = (fin_sec - inicio_sec) + 60*dif_min + 3600* dif_hora

		if fin_min > inicio_min and fin_sec < inicio_sec:
			dif_min = fin_min - inicio_min
			dif_sec = (60 - inicio_sec) + fin_sec + 60*(dif_min-1) + 3600*dif_hora

		if inicio_min > fin_min and fin_sec > inicio_sec:
			dif_min = (60-inicio_min)+fin_min + 3600*(fin_hora-1)
			dif_sec = fin_sec - inicio_sec + 60*dif_min			
		if inicio_min > fin_min and inicio_sec > fin_sec:
			
			dif_min = 60-inicio_min+fin_min+3600*(fin_hora-1)
			dif_sec = 60-inicio_sec+fin_sec+60*(dif_min-1)			
			

	
	nuevo.write(' '+str(dif_sec))





def calcular_duracion(horas1,horas2,nuevo,mavir):
	
	line2 = horas2.readline()
	k = 1
	while 1:
		
		line = horas1.readline()
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
				
				nuevo.write('mavir0'+mavir+'.wav '+time)
				diferencia_segundos(time,time2,nuevo)
				nuevo.write(' mavir0'+mavir+'_'+str(k)+'.wav\n')
			i = i+1 

		k = k+1


'''
inicio = input('Inicio: ')
print(len(inicio))

fin = input('Fin: ')
print(len(fin))

diferencia_segundos(inicio,fin)
'''























