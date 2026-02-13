print ("*************************************************")
print ("**Bienvenidos a la clase de fundamentos de python**")
print ("*************************************************")
#Variable de tipo string
#Variable int
#Variable Float
#Variable Boolean
#Operaciones con variables
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
peso = float(input("Ingrese su peso en kg: "))
es_estudiante = False
es_estudiante = input("¿Eres estudiante? (si/no): ").lower() == 'si'


print("Hola " + nombre + "Bienvenido a la clase de Fundamentos de Python")
print("Tus datos son los siguientes:")
print("Edad: " + str(edad))
print("Peso: " + str(peso) + " kg")
print("Es estudiante: " + str(es_estudiante))