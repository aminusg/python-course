"""
Ejercicio de Codificacion

In the below starter code, place 4 dog names (elements) of your choice in the dog_house list. Then write a while loop that iterates through the dog_house list and prints each dogs name. An iterator variable named "counter" must be set, and must have an initial value of 0.

Hint: An iterator value (also sometimes called a sentinel value) is a value that exists outside of your loop, and that you update or otherwise keep track of each time you loop, so that your while loop knows when to end.

Example:
iterator_value = 0
while iterator_value < 10:
    print("Keep looping...")
    iterator_value += 1
"""

#Ejemplos
nums = list(range(1, 100))

while len(nums) > 0:
  print(nums.pop())

def guessing_game():
  while True:
    print('What is your guess?')
    guess = input()

    if guess == '42':
      print('You correctly guessed it!')
      return False
    else:
      print(f"No, {guess} isn't the answer, please try again\n")

guessing_game()