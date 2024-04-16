#Exercise1: Cree un bucle For de Python

objects= ['gato', 'ventana', 'paracaidas']
for object in objects:
    print(object, len(object))



#Exercise2: Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3

def suma(a, b, c):
    return a+b+c
print(suma(3,56,74))

#EXERCISE3: Cree una función lambda con la misma funcionalidad que la función suma que acaba de crear.
suma= lambda a, b, c: a+b+c
resultado= suma(3,25,47)
print(resultado)

#Exercise4: Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista.
#Sugerencia: si es necesario utilice un bucle for in y el operador in.

nombre= 'Enrique'
lista_nombre= ['Jessica', 'Paul', 'George', 'Adan']
def coincidencia():
    exist= False
    for n in lista_nombre:
        if n == nombre:
            exist = True
            break
    if exist:
        print('El nombre coincide con uno de la lista')
    else:
        print('El nombre no coincide con ninguno de la lista')


coincidencia()