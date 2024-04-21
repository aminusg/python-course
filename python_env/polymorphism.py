#Vamos a crear una clase HTML, y podemos pensar en ello como en una clase que puede renderizar HTML en la pag
#Esta será la clase PADRE y la llamo simplemente Html. Dentro tendrá un método __init__
class Html:
    def __init__(self, content):
        self.content = content #Va a almacenar el contenido en la variable de instancia content
#Ahora vpy a crear una función abstracta llamada RENDER
    def render(self):             
        raise NotImplementedError("Subclass must implement render method") #Lo que estoy haciendo aquí es:
    #Si no quiero que el usuario final se conecte con esta clase  y que solo las clases hijas puedan llamar a la clase HTML

#Vamos a crear varias subclases que me permitirán renderizar versiones personalizadas de ese HTML
class Heading(Html):
    def render(self):
        return f'<h1>{self.content}</h1>'


class Div(Html):
    def render(self):
        return f'<div>{self.content}</div>'


tags = [
    Div('Some content'), 
    Heading('My Amazing Heading'), 
    Div('Another div')
    ]

for tag in tags:
    print(str(tag) + ': ' + tag.render()) #Aquí pruebo que todo está correcto
    
for tag in tags:
    print(tag.render())

"""
Así que en el polimorfismo lo que tenemos es que las clases hijas heredan el método de la clase padre 
pero luego anulan su comportamiento
"""