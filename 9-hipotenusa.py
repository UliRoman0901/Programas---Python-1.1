#Programa que imprime la suma de los cubos de n numeros
import math

print "----------------------------------------------------------"
print "-           Programa que calcula la hipotenusa           -"
print "----------------------------------------------------------"
print ""
print "INTRODUZCA EL VALOR DEL CATETO A: "
a = float(input())
print ""
print "INTRODUZCA EL VALOR DEL CATETO B: "
b = float(input())


print ""
print ".........................................................."
print "                        	RESULTADO                        "
print ""
print ""
def hipotenusa():
	print "CATETO A ES: ", a
	print "CATETO B ES: ", b

	hip = math.sqrt(a*a + b*b)

	print ""
	print "LA HIPOTENUSA ES: ", hip
	return

hipotenusa()

print ""
print ""
print "..........................................................."
print ""
print ""
print "Programa Finalizado"
print ""
