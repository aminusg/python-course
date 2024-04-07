# List of comparison operators
# == Equality
# != Inequality
# <> Inequality (deprecated)
# >  Greater than
# >= Greater than or equal to
# < Less than
# <= Less than or equal to

username = 'jonsnow'

if username == 'jonsnow':
  print('Welcome Jon')
else:
  print('You shall not pass!')

age = 25

if age <= 25:
  print(f"I'm sorry, you need to be at least 25 years old")

user_list = ['Kristine', 'Tiffany']
second_list = ['Kristine', 'Tiffany']

if user_list == second_list:
  print('They match')