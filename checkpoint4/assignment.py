#Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.
my_list= ['notebook', 'journal', 'diary', 'calender', 'notepad']

my_tuple= ('notebook', 'squared', 80)

my_float= 23.45

my_integer= 100

#para escribir el decimal tendré que importar la librería
from decimal import Decimal #esto lo pondría al comienzo del código)
my_decimal= Decimal(0.56)
print(my_decimal)

my_dictionary= {
    'Esther': 669445238,
    'María': 619236140,
    'Pedro': 669447669,
    'Carol': 630425132
}
#Exercise 2: Round your float up.
import math
print(math.ceil(my_float))

#Exercise 3: Get the square root of your float.
print(math.sqrt(my_float))

#Exercise 4: Select the first element from your dictionary.
first_element= list(my_dictionary.items())[0]
print(first_element)

#Exercise 5: Select the second element from your tuple.
segundo_elemento= my_tuple[1]
print(segundo_elemento)

#Exercise 6: Add an element to the end of your list.
my_list.append('sketchbook')
print(my_list)

#Exercise 7: Replace the first element in your list.
my_list[0]= 'folder'
print(my_list)

#Exercise 8: Sort your list alphabetically.
my_list.sort()
print(my_list)

#Exercise 9: Use reassignment to add an element to your tuple.
my_tuple= (my_tuple + ('recycled',))
print(my_tuple)