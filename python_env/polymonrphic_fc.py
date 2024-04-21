class Heading:    #En este caso no creamos una clase Padre, sino que ponemos la función init en las clases hijas que ahora serán independientes
    def __init__(self, content):
      self.content = content

    def render(self): #la dunción render la mantenemos iigual
      return f'<h1>{self.content}</h1>'

class Div:
  def __init__(self, content):
    self.content = content

  def render(self):
    return f'<div>{self.content}</div>'

div_one = Div('Some content') #aquí lo que hacemos es meter las tags en sus propias variables
heading = Heading('My Amazing Heading')
div_two = Div('Another div')

def html_render(tag_object):
  print(tag_object.render())

html_render(div_one)
html_render(div_two)
html_render(heading)