# Uno de desafío 3.

# 5) La siguiente matriz (o lista con listas anidadas) debe cumplir una condición: en cada fila el cuarto elemento siempre debe ser el resultado de sumar los tres primeros. ¿Eres capaz de modificar la matriz inicial usando la técnica del slicing?

# 🖐 Ayuda:  La función llamada sum(lista) devuelve una suma de todos los elementos de la lista

# Partirás de: 
# matriz = [ 
#     [1, 5, 1],
#     [2, 1, 2],
#     [3, 0, 1],
#     [1, 4, 4]
# ]

# # Debes llegar a: 
# matriz = [ 
#     [1, 5, 1, 7],
#     [2, 1, 2, 5],
#     [3, 0, 1, 4],
#     [1, 4, 4, 9]
# ]

# # Respuesta
# matriz = [ 
#     [1, 5, 1],
#     [2, 1, 2],
#     [3, 0, 1],
#     [1, 4, 4]
# ]
# matriz[0][len(matriz[0]):]=[sum(matriz[0])]
# matriz[1][len(matriz[1]):]=[sum(matriz[1])]
# matriz[2][len(matriz[2]):]=[sum(matriz[2])]
# matriz[3][len(matriz[3]):]=[sum(matriz[3])]
# print(matriz)
# #otra posible solución sería
# matriz[0].append(sum(matriz[0]))
# matriz[1].append(sum(matriz[1]))
# matriz[2].append(sum(matriz[2]))
# matriz[3].append(sum(matriz[3]))
# print(matriz)
# ------------------------------------------

# Ejercicios desafío 4----------------------
# Num1= float(input("ingrese el primer número: "))
# Num2= float(input("ingrese el segundo número: "))
# opcion= int(input("Ingrese una opción del 1 al 4 depende que resultado quiera: "))
# # 1. Mostrar una suma de los dos números
# # 2. Mostrar una resta de los dos números (el primero menos el segundo)
# # 3. Mostrar una multiplicación de los dos números
# # 4. Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
# # En caso de no introducir una opción válida, el programa informará de que no es correcta.
# if opcion >= 1 and opcion <= 4 :
#     if opcion == 1:
#       print(f"la suma es: {Num1+Num2}")
#     elif opcion == 2:
#       print(f"la resta es: {Num1-Num2}")
#     elif opcion == 3:
#         print(f"la resta es: {Num1-Num2}")
#         print(f"el producto de ambos números es: {Num1*Num2}")
#     else:
#       print("el programa ha finalizado")
# else:
#   print("El número elegido es incorrecto ya que no es ninguna de las opciones permitidas, por favor vuelva a intentarlo")


# num= int(input("Ingrese un Número entero: "))
# while num%2==0:
#   num=int(input("Ingrese otro numero entero: "))
# else: 
#   print(f"el numero impar es {num}")
   
# valor= sum(range(1,100,2))
# print (valor)

# suma = 0
# var = 0
# q= int(input("ingrese la cantidad de números a ingresar: "))
# for var in range(q):
#   suma+= int (input("Ingrese número:"))
 
# media = suma / q
# print(f"la media es {media}")

# numeros = [1, 3, 6, 9]
# numeros = [1, 3, 6, 9]
# lista= list(range(0,10))
# var = int(input("Ingrese un numero entero entre el 0 y el 9: "))
# while not var in lista:
#   var = int (input("Valor mal ingresado, por favor que sea entre en 0 y el 9: "))  
# else:
#   if var in numeros:
#     print ("true")
#   else:
#     print ("el valor no está en la lista numeros")


# lista1=list(range(0,11))
# print(lista1)
# lista2=list(range(-10,1))
# print(lista2)
# lista3=list(range(0,21,2))
# print(lista3)
# lista4=list(range(-19,0,2))
# print(lista4)
# lista5=list(range(0,51,5))
# print(lista5)

# lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
# lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
# lista_3 = []
# for x in lista_1:
#   if x in lista_2 and x not in lista_3:
#     lista_3.append(x)
# print(lista_3)
# ---------------------------------------------------------------

#Año bisiesto
# def bisiesto (año):
#   if type (año) != int:
#     return "No ingresaste un año"
#   if año % 4 !=0:
#     return "El año no es bisiesto"
#   elif año % 4 == 0 and año % 100 != 0:
#     return "El año si es bisiesto"
#   elif año % 4 != 0 and año % 100 == 0 and año % 400 != 0:
#     return "El año no es bisiesto"
#   elif año % 4 == 0 and año % 100 != 0 and año % 400 == 0:
#     return "El año si es bisiesto"

# print(bisiesto(2024))
# print(bisiesto(2007))
# print(bisiesto(2020))
# print(bisiesto(1987))
# print(bisiesto("Hola"))

#Otro ejemplo
# def año_bisiesto(año):
#   if ( type(año) != int):
#     print("el parametro ingresado no es un año!")
#   else:
#     if ( año % 4 == 0) and (año % 100 != 0) or (año % 400 == 0):
#       print("Es un año Biciesto")
#     else:
#       print("No es un año Biciesto")
#   return(año_bisiesto)
# año_bisiesto(2015)

#Otro ejemplo-----------------------
# def Si_Bisiesto(Año):
#         if((Año % 400 == 0) or
#            (Año % 100 != 0) and
#            (Año % 4 == 0)):
#             print("Es un año Bisiesto");
#         else:
#             print("No es un año Bisiesto")
# while True:
#     try:
#         Año = int(input("ingresa un año: "))
#     except ValueError:
#         print("revise los datos ingresados e ingrese un año")
#         continue
#     else:
#         break
# Si_Bisiesto(Año)

#Otro ejemplo--------------------------
# def año_bisiesto(año):
#   if type(año)==str:
#     return print ('El parámetro ingresado no es un año, por favor ingrese un número válido')
#   elif año%4!=0 or (año%100==0 and año%400!=0):
#     return print (f'El año {año} no es bisiesto')
#   else:
#     return print (f'El año {año} es bisiesto')


# año_bisiesto(2012)
# año_bisiesto(2010)
# año_bisiesto(2000)
# año_bisiesto(1900)
# año_bisiesto('2000')



#Ejercico de reloj//////
# def reloj(*args):

#   if len(args)!=1 and len(args)!=3:
#     print("esta funcion solo se usa con 1 o 3 argumentos")
#   elif len(args)==1:
#     segundos=args[0]

#     horas=segundos//3600 #cantidad exacta de horas
#     resto=segundos%3600  #lo que tengo que seguir dividiendo

#     minutos=resto//60   #cantidad exacta de minutos
#     segundos=resto%60   #cantidad exacta de segundos
#     print(f"son {horas} horas, {minutos} minutos y {segundos} segundos")
#   else:
#     horas=args[0]
#     minutos=args[1]
#     segundos=args[2]

#     segundos=horas*3600+minutos*60+segundos
#     print(f"son {segundos} segundos")

#Ejercicio 
# def recortar (valor, inferior, superior):
#   if valor >= superior:
#     resultado = superior
#   elif valor <= inferior:
#     resultado = inferior
#   else: 
#     resultado = valor
#   return resultado
 
# resultado = recortar(15, 0, 10)
# print(resultado)

#Otro ejemplo del mismo ejercicio anterior
# def recortar(num,lim_inf,lim_sup):
#   if num>lim_sup:
#     return print(lim_sup)
#   elif num<lim_inf:
#     return print(lim_inf)
#   else:
#     return print(num)
    
# recortar(15,0,10)


#Ejercicio de separar
# def separar(lista):
#   pares = []
#   impares = []
#   for n in lista:
#     print(n)
#     if n % 2 == 0:
#       pares.append(n)
#     else:
#       impares.append(n)
#   return pares, impares

