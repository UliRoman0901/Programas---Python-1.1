#Programa que imprime la suma de los cubos de n numeros
print "----------------------------------------------------------"
print "- Programa que imprime la suma de los cubos de n numeros -"
print "----------------------------------------------------------"
print ""
print "INTRODUZCA EL NUMERO: "
num = input()
print ""
print "........................................................"
print "                        RESULTADO                       "
print ""

def sumacubos():
	i = 1
	contador = 1
	suma = 0.0
	n = 1
	lista = []
	while contador<=num:
	
		n = i ** 3
		suma = suma + n
		i += 1
		contador += 1
		lista.append(n)
		#print (n)

	print ""	
	print "Lista de numeros: ", lista
	print "suma de numeros: ", suma
	return	
sumacubos()
print ""
print "........................................................."
print ""
print "Programa finalizado           "
print ""