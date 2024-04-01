"""
heading_generator(title, heading_type)
heading_generator('Greeting', '1')
<h1>Greeting</h1>

heading_generator('Hi there', '3')
<h3>Hi there</h3>

"""
def heading_generator(title, heading_type):
    return f'<h{heading_type}>{title}</h{heading_type}'

mi_h1 = heading_generator('Greeting', '1')
print(mi_h1)

mi_h3= heading_generator('Hi there', '3')
print(mi_h3)
