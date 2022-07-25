# Basic_Python
### Repositorio de diferentes archivos en Python
Descripción: Lo que pretendo con este repositorio es acumular diferentes algorimos básicos que sean de referencia o notas para futuras consultas. A continución, se lanzan diferes comandos usando la libreria de Numpy para crear vectores y matrices.  

# Escribiendo código

La primer línea del archivo.
    
    import numpy as np

# Más de matrices

    a = np.array([1,2,3,4,5,6])

conocer la dimensión de a

    print("La dimensión de 'a' = {} es: {}".format(a, a.shape))

Se puede expandir la dimensión utilisando la funsión np.expand_dims()
con axis=0, expande hacia las filas, con axis=1, expande hacia las columnas.

    b = np.expand_dims(a, axis=0) # Vector fila
    c = np.expand_dims(a, axis=1) # Vector columna

Se imprime el resultado

    print("\nDimensiones de 'a': {}, 'b': {} y 'c': {}".format(a.shape, b.shape, c.shape))

Creo una Matriz

    x = np.array([[1,2],[3,4],[5,6]])
    print("Escribe la matriz x:\n {}".format(x))

Presentación de una sub-matris de x:

    print("Presentación de una sub-matriz de x:\n {} ".format(x[np.array([1,-1])]))

Creación de un vector pero redimencionandolo a matriz

    y = np.arange(35).reshape(5,7)


# Funciones
A continuación ser presenta dos formas de hacer un switch.
Se crea una función que recibe dos números y tambien la operación matemática.
Primera forma de hacer un switch (con if). Se invoca de la siguiente manera, ejemplo: *opera1(suma,3,6)*.

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

La segunda forma de hacer un switch es con la función *lambda* y se invoca de la siguiente manera, ejemplo: *opera2(suma,3,6)()*
    
    def opera2(operador, a, b): 
        return {
            'suma': lambda: a + b,
            'resta': lambda: a - b,
            'multiplica': lambda: a * b,
            'divide': lambda: a / b
        }.get(operador, lambda: None)

Veamos algunas operaciones:

    print("la suma de 3 + 4 es: {}".format(opera1('suma',3,4)))
    print("la resta de 5 - 2 es: {}".format(opera1('resta',5,2)))
    print("la división de 15 / 3 es: {}".format(opera2('divide',15,3)()))
    print("la multiplicación de 7 * 9 es: {}".format(opera2('multiplica',7,9)()))


# funcion zip()
La función *zip()*, une dos elementos de dos listas diferentes en sus mismas posiciones.
Veamos un ejemplo:

    a=[3,4,5]
    b=["tres", "cuatro", "cinco"]
    c=zip(a,b)
    print("\nse une dos listas\n Lista uno: {} \n Lista dos: {}".format(a,b))
    print("listas comprimidas: ")
    print(list(c))

# enumarate() en Python
La funcion enumerate(), enumera desde el valor cero (0) todos los elementos de una lista.
Como lo haría la funcion zip() con una lista cualquiera a la que le añade la posición a cada elemento.

    print("\nListando la lista con sus índices") 
    letras = ["A","B","C"]
    indice = 0
    for indice, l in enumerate(letras): 
        print(indice,l)
        indice +=1

# List comprehesions
sintanxis: lista = [ *expresión* for *elemento* in *iterable* if *condición* ]

Forma tradicional usando un *for*

    cuadrados = []
    for i in range(5):
        cuadrados.append(i**2)

    print("\nLista de los cuadrados: {}".format(cuadrados))

# Usando list comprehesion

    print("\nLista de los cuadrados usando 'list comprehesion': {}".format([i**2 for i in range(5)]))

list comprehesion con condicionales

    frase = "El perro de san roque no tiene rabo"
    erres = [i for i in frase if i=='r']
    print("\nLas erres en la frase '{}' son: {}".format((frase),len(erres)))
