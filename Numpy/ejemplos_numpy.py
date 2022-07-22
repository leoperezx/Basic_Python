import numpy as np

# esto es una lista 
lista = list(range(0,10))
# la respuesta es >>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# esto es un array
arr = np.arange(0,10)
# la respuesta es >>> [0 1 2 3 4 5 6 7 8 9]

print(lista,arr)

# crea un vector de 0 a 18 de dos en dos.
arr1 = np.arange(0,20,2)

# crea un vector de ceros de 1x10
ceros = np.zeros(10)

print("Vector de 0 a 18 de dos en dos: {} ".format(arr1))
print("Vector de ceros de 1x10: {} ".format(ceros))

# crea una matriz de 3x3 de ceros 
Mceros = np.zeros((3,3))
Munos = np.ones((5,3))

print("Matriz de ceros de 3x3: \n {} ".format(Mceros))
print("Matriz de unos de 5x3: \n {} ".format(Munos))

# es como pedir 10 datos de 0 a 100
lineas10 = np.linspace(0,100,10)
# es como pedir 100 datos de 0 a 10
lineas100 = np.linspace(0,10,100)

# Adicionar, remomer y organizar elementos
arr = np.array([2,1,5,3,7,4,6,8])
# organizando los numeros
arr_sort = np.sort(arr)

print("Vector original en desorden: {}\n".format(arr))
print("Vector con sus elementos ordenados: {}\n".format(arr_sort))

# Concatenar vectores

a=np.array([1,2,3,4])
b=np.array([5,6,7,8])

c=np.concatenate((a,b))
print("Vector a = {} | Vector b = {}".format(a,b))
print("\nConcatenando a y b = {}".format(c))

# Filtrando valores dentro del vector
# Se crea la condición
five_up = (c > 5) 
# Se imprime con la condición
print("\nSe imprime el vector c pero solo los valores mayores a 5: {}".format((c[five_up])))


# matriz diagonal de unos
Mdiagonal = np.eye(7)

print("\nVector de 1x10 con valores de 0 a 100 equidistantes: \n {} ".format(lineas10))
print("Vector de 1x100 con valores de 0 a 10 equidistantes: \n {} ".format(lineas100))

print("\nMatriz diagonal de unos: \n {} ".format(Mdiagonal))

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print("\nVector o Matriz?: \n {} ".format(a))
# se construye como un vector, pero es una matriz

# invoacndo los valores
print("llamando a toda la final 1: \n {} ".format(a[0]))
print("llamando a toda la final 3: \n {} ".format(a[2]))
print("llamando a toda la columna 1: \n {} ".format(a[:,0]))

# Iteradores 
# for es un iterador

# range es un objeto iterable tiene 5 campos que va de 0 a 4
vector = range(0,5)
print(vector)
print(type(vector))
for i in vector:
    print(i)
# la cadena de caracteres "Python" es un objeto iterable
print("Python")
for i in "Python":
    print(i)

lista = [5,6,7,8] # lista es un iterable
it = iter(lista) # iter es una funcion para iterar lista por medio de la funcion next()
# la funcion next(), es independiente por objeto y solo trabaja en un sentido, 
# solo se puede hacer una vez y en un sentido que es del primer elemento al último.

print("primer elemento de 'it': {} ". format(next(it)))
print("5 es el primer número de el objeto iterable 'it'")
print("invoco al segundo elemento de 'it': {} ".format(next(it)))

# primera forma de hacer un switch (con if)
# se invoca de la siguiente manera 
# >>> opera1(suma,3,6)
def opera1(operador, a, b):
    if operador == 'suma':
        return a + b
    elif operador == 'resta':
        return a - b
    elif operador == 'multiplica':
        return a * b
    elif operador == 'divide':
        return a / b
    else:
        return None
# segunda forma de hacer un switch (con función lambda)
# se invoca de la siguiente manera
# >>> opera2(suma,3,6)()
def opera2(operador, a, b): 
    return {
        'suma': lambda: a + b,
        'resta': lambda: a - b,
        'multiplica': lambda: a * b,
        'divide': lambda: a / b
    }.get(operador, lambda: None)

print("la suma de 3 + 4 es: {}".format(opera1('suma',3,4)))
print("la resta de 5 - 2 es: {}".format(opera1('resta',5,2)))
print("la división de 15 / 3 es: {}".format(opera2('divide',15,3)()))
print("la multiplicación de 7 * 9 es: {}".format(opera2('multiplica',7,9)()))


# funcion zip()
a=[3,4,5]
b=["tres", "cuatro", "cinco"]
c=zip(a,b)
print("\nse une dos listas\n Lista uno: {} \n Lista dos: {}".format(a,b))
print("listas comprimidas: ")
print(list(c))

# enumarate() en Python
# La funcion enumerate(), enumera desde el valor cero (0) todos los elementos de una lista
# como lo haría la funcion zip()

print("\nListando la lista con sus índices") 
letras = ["A","B","C"]
indice = 0
for indice, l in enumerate(letras): 
    print(indice,l)
    indice +=1

# List comprehesions
# sintanxis: lista = [<expresión> for <elemento> in <iterable> if <condición>]

cuadrados = []
for i in range(5):
    cuadrados.append(i**2)

print("\nLista de los cuadrados: {}".format(cuadrados))

# usando list comprehesion
print("\nLista de los cuadrados usando 'list comprehesion': {}".format([i**2 for i in range(5)]))

# list comprehesion con condicionales
frase = "El perro de san roque no tiene rabo"
erres = [i for i in frase if i=='r']
print("\nLas erres en la frase '{}' son: {}".format((frase),len(erres)))

