username = 'jonsnow'
email = 'jon@snow.com'
password = 'thenorth'

if username == 'jonsnow' and password == 'thenorth':
  print('Access permitted')
else:
  print('Not allowed')


if (username == 'jonsnow' or email == 'jon@snow.com') and password == 'thenorth':
  print('Access permitted')
else:
  print('Not allowed')


if username == 'jonsnow' or password == 'thenorth':
  print('Access permitted')
else:
  print('Not allowed')


logged_in = True
standard_user = False

if logged_in and not standard_user:
  print('You can access the admin dashboard')
else:
  print('You can only access the standard dashboard')


#Fill in the below conditional with a compound condition that will print "Success!" if "number" is anything between 1 and 100 (inclusive).
number = range(1, 101)
def compound_conditional(number):
   if number in range(1, 101) and number % 2 == 0:  # Se agrega la condición number % 2 == 0 para comprobar si el número es par
        print("Success!")
   else:
        print("Failure...")

compound_conditional(5)