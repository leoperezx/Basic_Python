# Basic_Python
### Repositorio de diferentes archivos en Python
Descripción: Lo que pretendo con este repositorio es acumular diferentes algorimos básicos que sean de referencia o notas para futuras consultas. A continución, se lanzan diferes comandos usando la libreria de Numpy para crear vectores y matrices.  

# escribiendo código

La primer línea del archivo.
    import numpy as np

Esto es una lista. 
    lista = list(range(0,10))
    # La respuesta es >>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Nota que no incluye el 10

Esto es un array.
    arr = np.arange(0,10)
    # La respuesta es >>> [0 1 2 3 4 5 6 7 8 9].
    # Nota que no incluye el 10

    print(lista,arr)

Crea un vector de 0 a 18 de dos en dos.
    arr1 = np.arange(0,20,2)

Crea un vector de ceros de 1x10.
    ceros = np.zeros(10)
    # Imprime los vectores utilizando un formato para el print.
    print("Vector de 0 a 18 de dos en dos: {} ".format(arr1))
    print("Vector de ceros de 1x10: {} ".format(ceros))

Crea una matriz de 3x3 de ceros.
    Mceros = np.zeros((3,3))
    Munos = np.ones((5,3))
    # Imprime las matrices utilizando un formato para el print.
    # Se utiliza el \n para hacer un salto de línea.
    print("Matriz de ceros de 3x3: \n {} ".format(Mceros))
    print("Matriz de unos de 5x3: \n {} ".format(Munos))

Crea un vector pero, es como pedir 10 datos de 0 a 100
    lineas10 = np.linspace(0,100,10)

Crea un vector pero, es como pedir 100 datos de 0 a 10
    lineas100 = np.linspace(0,10,100)

    # Imprime las los vectores utilizando un formato para el print
    print("Vector de 1x10 con valores de 0 a 100 equidistantes: \n {} ".format(lineas10))
    print("Vector de 1x100 con valores de 0 a 10 equidistantes: \n {} ".format(lineas100))

Crea una matriz diagonal de unos
    Mdiagonal = np.eye(7)
    # se utiliza el \n para hacer un salto de línea
    print("Matriz diagonal de unos: \n {} ".format(Mdiagonal))

    a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    print("Vector o Matriz?: \n {} ".format(a))
se construye como un vector de vectores, pero es una matriz

# invocando los valores
Veamos como invocar sus valores:
    print("llamando a toda la final 1: \n {} ".format(a[0]))
    print("llamando a toda la final 3: \n {} ".format(a[2]))
    print("llamando a toda la columna 1: \n {} ".format(a[:1]))

# Iteradores 
for es un iterador y necesita un iterable.
*range* crea un objeto iterable que tiene 5 campos que va de 0 a 4
    vector = range(0,5)
    print(vector)
    for i in vector:
        print(i)

la cadena de caracteres *Python* es un objeto iterable
    print("Python")
    for i in "Python":
        print(i)

Las *listas* son iterables 
    lista = [5,6,7,8] # lista es un iterable
    it = iter(lista) # iter es una funcion para iterar lista por medio de la funcion next()

La funcion *next()*, se utiliza para iterar es independiente por objeto y solo trabaja en un sentido, 
solo se puede hacer una vez y en un sentido que es del primer elemento al último.
    print("primer elemento de 'it': {} ". format(next(it)))
    print("5 es el primer número de el objeto iterable 'it'")
    print("invoco al segundo elemento de 'it': {} ".format(next(it)))
