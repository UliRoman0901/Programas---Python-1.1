#Programa que imprime la suma de los cuadrados de n numeros 
print "--------------------------------------------------------------"
print "- Programa que imprime la suma de los cuadrados de n numeros -"
print "--------------------------------------------------------------"


def sumacuadrados():
	print ""
	print ""
	print "Cuantos numeros quieres generar: "
	num = input()
	print ""
	print ""
	i = 1
	contador = 1
	suma = 0.0
	n = 1
	lista = []
	while contador<=num:
	
		n = i ** 2
		suma = suma + n
		i += 1
		contador += 1
		lista.append(n)
		#print (n)
	print "........................................................"
	print "                        RESULTADO                       "
	print ""	
	print ""	
	print "Lista de numeros: ", lista
	print ""
	print "suma de numeros: ", suma	
	print ""
	print ""
	print "........................................................."
	print ""
	print ""
	print "Escribe 1 si quieres crear otra lista, de lo contrario escribe cualquier numero:"
	k = input()
	if k == 1:
		sumacuadrados()
	else:
		print ""
		print "Gracias por usar este programa :)"
		print ""
	return

sumacuadrados()


print ""
print ""
print "Programa Finalizado"
print ""