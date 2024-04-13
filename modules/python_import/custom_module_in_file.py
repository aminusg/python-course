#para importar librerías que están en otros directorios,
import sys
sys.path.insert(0, './python_import/libs')
import helper


def render():
    print(helper.greeting('Kristine', 'Hudgens'))

render()
