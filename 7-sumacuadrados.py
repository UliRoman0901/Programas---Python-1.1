#Programa que imprime la suma de los cuadrados de n numeros mayores a 100
print "---------------------------------------------------------------------------"
print "- Programa que imprime la suma de los cuadrados de n numeros mayores a 100-"
print "---------------------------------------------------------------------------"
print ""
print "INTRODUZCA EL NUMERO: "
num = input()
print ""
print "..............................................................."
print "                            RESULTADO"
print ""

def sumacuadrados():
	i = 101
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
	print ""	
	print "Lista de numeros: ", lista
	print "suma de numeros: ", suma	
	return
sumacuadrados()

print ""
print "..............................................................."
print ""
print "Programa Finalizado"
print ""