import funciones as f


#Primero elimino los archivos existentes
f.eliminar_archivos_existentes()

mavir = open('../original/mavir02.txt','r')
mavir1 = open('../nuevo/mavir02_new.txt','w')

#Elimino caracteres especiales simples
f.eliminar_especiales(mavir,mavir1)
	
mavir.close()
mavir1.close()

mavir = open('../nuevo/mavir02_new.txt','r')
mavir1 = open('../nuevo/mavir02_new2.txt','w')

#Elimino strings hhh
f.eliminar_letras(mavir,mavir1,'h')

mavir.close()
mavir1.close()

mavir = open ('../nuevo/mavir02_new2.txt','r')
mavir1 = open('../nuevo/mavir02_new3.txt','w')

#Elimino strings xxx
f.eliminar_letras(mavir,mavir1,'x')

mavir.close()
mavir1.close()


mavir = open('../nuevo/mavir02_new3.txt','r')
mavir1 = open('../nuevo/mavir02_new4.txt','w')

#Elimino marcas derivadas de &
f.eliminar_amp(mavir,mavir1)

mavir.close()
mavir1.close()

mavir = open('../nuevo/mavir02_new4.txt','r')
mavir1 = open('../nuevo/mavir02_new5.txt','w')

#Elimino comentarios
f.eliminar_comentarios(mavir,mavir1)

mavir.close()
mavir1.close()


mavir = open('../nuevo/mavir02_new5.txt','r')
mavir1 = open('../nuevo/mavir02_new6.txt','w')

#Elmimino nombres de los participantes
f.eliminar_nombres(mavir,mavir1)

mavir.close()
mavir1.close()




