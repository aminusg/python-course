sentence = 'The quick brown fox jumped over the lazy Dog'
word = 'dog'

if word.lower() in sentence.lower():
  print('The word is in the sentence')
else:
  print('The word is not in the sentence')


nums = [1, 2, 3, 4]

if 3 in nums:
  print('The number was found')
else:
  print('The number was not found')


#In the below code, fix the condition so that the program prints out "The word is in the sentence".
def value_in_string():
    sentence = 'Python is the best!'
    value = 'best'
    if value in sentence:
      print('The word is in the sentence')
    else:
      print('The word is not in the sentence')
value_in_string()