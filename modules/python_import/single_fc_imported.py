import sys
sys.path.insert(0, './python_import/libs')
from helper import greeting


def render():
    print(greeting('Kristine', 'Hudgens'))

render()
