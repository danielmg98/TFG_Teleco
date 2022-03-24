import funciones as f

#Primero elimino los archivos existentes

i = input('Que archivo mavir desea traducir: ')


f.eliminar_archivos_existentes(i)

mavir = open('../original/mavir0'+i+'.txt','r')
mavir1 = open('../nuevo/mavir0'+i+'/mavir0'+i+'_new.txt','w')

#Elimino caracteres especiales simples
f.eliminar_especiales(mavir,mavir1)
	
mavir.close()
mavir1.close()

mavir = open('../nuevo/mavir0'+i+'/mavir0'+i+'_new.txt','r')
mavir1 = open('../nuevo/mavir0'+i+'/mavir0'+i+'_new2.txt','w')

#Elimino strings hhh
f.eliminar_letras(mavir,mavir1,'h')

mavir.close()
mavir1.close()

mavir = open('../nuevo/mavir0'+i+'/mavir0'+i+'_new2.txt','r')
mavir1 = open('../nuevo/mavir0'+i+'/mavir0'+i+'_new3.txt','w')

#Elimino strings xxx
f.eliminar_letras(mavir,mavir1,'x')

mavir.close()
mavir1.close()


mavir = open('../nuevo/mavir0'+i+'/mavir0'+i+'_new3.txt','r')
mavir1 = open('../nuevo/mavir0'+i+'/mavir0'+i+'_new4.txt','w')


#Elimino marcas derivadas de &
f.eliminar_amp(mavir,mavir1)

mavir.close()
mavir1.close()

mavir = open('../nuevo/mavir0'+i+'/mavir0'+i+'_new4.txt','r')
mavir1 = open('../nuevo/mavir0'+i+'/mavir0'+i+'_new5.txt','w')

#Elimino comentarios
f.eliminar_comentarios(mavir,mavir1)

mavir.close()
mavir1.close()


mavir = open('../nuevo/mavir0'+i+'/mavir0'+i+'_new5.txt','r')
mavir1 = open('../nuevo/mavir0'+i+'/mavir0'+i+'_new6.txt','w')

#Elmimino nombres de los participantes
f.eliminar_nombres(mavir,mavir1)

mavir.close()
mavir1.close()

mavir = open('../nuevo/mavir0'+i+'/mavir0'+i+'_new6.txt','r')
mavir1 = open('../nuevo/mavir0'+i+'/mavir0'+i+'_new7.txt','w')

#Elimino espacios sobrantes
f.eliminar_espacios(mavir,mavir1)

mavir.close()
mavir1.close()

mavir = open('../nuevo/mavir0'+i+'/mavir0'+i+'_new7.txt','r')
mavir1 = open('../nuevo/mavir0'+i+'/mavir0'+i+'_new8.txt','w')

#Elimino sangrias
f.eliminar_espacios_inicio(mavir,mavir1)

mavir.close()
mavir1.close()

mavir = open('../nuevo/mavir0'+i+'/mavir0'+i+'_new8.txt','r')
mavir1 = open('../nuevo/mavir0'+i+'/mavir0'+i+'_new9.txt','w')

#Paso a palabra por linea
f.cambiar_espacios_lineas(mavir,mavir1)

mavir.close()
mavir1.close()


mavir = open('../nuevo/mavir0'+i+'/mavir0'+i+'_new9.txt','r')
mavir1 = open('../nuevo/mavir0'+i+'/mavir0'+i+'_new10.txt','w')

#Cambiar tiempos por puntos
f.cambiar_horas_puntos(mavir,mavir1)

mavir.close()
mavir1.close()


mavir = open('../nuevo/mavir0'+i+'/mavir0'+i+'_new10.txt','r')
mavir1 = open('../nuevo/mavir0'+i+'/mavir0'+i+'_new11.txt','w')

#Cambiar puntos por labels
f.formato_htk(mavir,mavir1,i)

mavir.close()
mavir1.close()
