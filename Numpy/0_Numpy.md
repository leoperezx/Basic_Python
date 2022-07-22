# Basic_Python
### Repositorio de diferentes archivos en Python
Descripción: Lo que pretendo con este repositorio es acumular diferentes algorimos básicos que sean de referencia o notas para futuras consultas. A continución, se lanzan diferes comandos usando la libreria de Numpy para crear vectores y matrices.  

# Escribiendo código

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
    
Imprime los vectores utilizando un formato para el print.

    print("Vector de 0 a 18 de dos en dos: {} ".format(arr1))
    print("Vector de ceros de 1x10: {} ".format(ceros))

Crea una matriz de 3x3 de ceros.
    
    Mceros = np.zeros((3,3))

Crea una matriz de 5x3 de unos.    
    
    Munos = np.ones((5,3))

Imprime las matrices utilizando un formato para el print.

    # Se utiliza el \n para hacer un salto de línea.
    print("Matriz de ceros de 3x3: \n {} ".format(Mceros))
    print("Matriz de unos de 5x3: \n {} ".format(Munos))

Crea un vector pero, es como pedir 10 datos de 0 a 100.
    
    lineas10 = np.linspace(0,100,10)

Crea un vector pero, es como pedir 100 datos de 0 a 10.
    
    lineas100 = np.linspace(0,10,100)
    
Imprime las los vectores utilizando un formato para el print con la opción de \n.

    print("Vector de 1x10 con valores de 0 a 100 equidistantes: \n {} ".format(lineas10))
    print("Vector de 1x100 con valores de 0 a 10 equidistantes: \n {} ".format(lineas100))

Adicionar, remomer y organizar elementos

    arr = np.array([2,1,5,3,7,4,6,8])

Organizando los numeros

    arr_sort = np.sort(arr)

    print("Vector original en desorden: {}\n".format(arr))
    print("Vector con sus elementos ordenados: {}\n".format(arr_sort))

Concatenar vectores

    a=np.array([1,2,3,4])
    b=np.array([5,6,7,8])

    c=np.concatenate((a,b))
    
    print("Vector a = {} | Vector b = {}".format(a,b))
    print("\nConcatenando a y b = {}".format(c))

Filtrando valores dentro del vector creando la condición

    five_up = (c > 5) 

Se imprime con la condición

    print("\nSe imprime el vector c pero solo los valores mayores a 5: {}".format((c[five_up])))

# Matrices

Crea una matriz diagonal de unos y se imprime.
    
    Mdiagonal = np.eye(7)
    # se utiliza el \n para hacer un salto de línea
    print("Matriz diagonal de unos: \n {} ".format(Mdiagonal))

Se Crea un vector de vectores pero, es una matriz. Esta se imprime.

    a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    print("Vector o Matriz?: \n {} ".format(a))


# invocando los valores de una matríz

Tomando como ejemplo la matriz anterior, tenemos:

    [[ 1  2  3  4]
    [ 5  6  7  8]
    [ 9 10 11 12]]

Veamos como invocar sus valores:
    
    # (x,y) donde *x* es la fila y *y* son las columnas
    # El simbolo : indica todos sus valores
    print("llamando a toda la final 1: \n {} ".format(a[0]))
    print("llamando a toda la final 3: \n {} ".format(a[2]))
    print("llamando a toda la columna 2: \n {} ".format(a[:,1]))
    print("llamando a toda la columna 1: \n {} ".format(a[:,0]))
    print("llamando a la fila 3 y columna 0: \n {} ".format(a[2,0]))

# Iteradores 

El ciclo *for* es un iterador que necesita un iterable para realizar su operación de pasar por cada uno de los elementos. 
La función *range()* crea un objeto iterable que tiene 5 campos que va de 0 a 4.
    
    vector = range(0,5)
    print(vector)
    for i in vector:
        print(i)

La cadena de caracteres *Python* es un objeto iterable por lo cual se puede usar con *for*.
    
    print("Python")
    for i in "Python":
        print(i)

Las *listas* también son iterables. 
    
    lista = [5,6,7,8] # lista es un iterable
    it = iter(lista) # iter es una funcion para iterar lista por medio de la funcion next()

La funcion *next()*, se utiliza para iterar es independiente por objeto y solo trabaja en un sentido, 
solo se puede hacer una vez y en un sentido que es del primer elemento al último.
    
    print("primer elemento de 'it': {} ". format(next(it)))
    print("5 es el primer número de el objeto iterable 'it'")
    print("invoco al segundo elemento de 'it': {} ".format(next(it)))