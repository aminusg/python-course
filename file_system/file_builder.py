file_builder = open('logger.txt', 'w+')
#open es una función general integrada en el lenguaje python que nos va a permitir crear o abrir un archivo
#si la función encuentra un archivo llamado así lo abre, si no, lo crea

#Ahora veremos cómo añadir contenido dinámicamente a ese archivo
file_builder.write("Hey, I'm in a file")
#.write es una función dentro de la biblioteca de archivos de Python
#para ver lo que hemos escrito, primero debemos cerrar el archivo, así que llamamos a la función close que no necesita ningún argumento
file_builder.close()

file_builder = open("logger.txt", "w+")

for i in range(100):
    file_builder.write(f"I'm on line {i + 1}\n") #\n lo que hace es que en cada iteración hace un enter


# file_builder.write("Hey, I'm in a file!")

file_builder.close()