# List: []
# Dictionary: {}
# Tuple: ()

# Tuple: immutable 
# List: mutable

post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

# Tuple unpacking
title, sub_heading, content = post

# Equivalent to Tuple unpacking
# title = post[0]
# sub_heading = post[1]
# content = post[2]

print(title)
print(sub_heading)
print(content)

#Example of something we can't do with tuples
"""post = ['Python Basics', 'Intro guide to python', 'Some cool python content']
post.sort()
#al ser una lista nos ordenaría por orden alfabético y dejaría de asignar el título con el título el subtítulo etc.
"""
"""
post = ('Python Basics', 'Intro guide to python', 'Some cool python content')
en cambio con una tuple nos daría error si hiciéramos post.sort() porque las tuplas no se pueden modificar
"""
