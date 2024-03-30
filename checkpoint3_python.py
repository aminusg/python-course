#Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.
#String
message= "Hello friends!"
print(message)
#number
invitados= 20
print(invitados)
#list
elementos=[1,2,"autogiro"]
print(elementos)
#boolean
encendido= True

#Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable. 
sentence= "many hands make light work"
first_three_letters= sentence[0:3]
print(first_three_letters)

#Exercise 3: Use an index to grab the first element from your list.
first_element= elementos[0]
print(first_element)

#Exercise 4: Create a new number variable that adds 10 to your original number.
new_number= invitados + 10
print(new_number)

#Exercise 5: Use an index to get the last element in your list.
last_element= elementos[-1]
print(last_element)

#Exercise 6: Use split to transform the following string into a list.
names= "harry,alex,susie,jared,gail,conner"
list_of_names= names.split(",")
print(list_of_names)

#Exercise 7: Get the first word from your string using indexes. Use the upper function to transform the letters into uppercase. Create a new string that takes the uppercase word and the rest of the original string.
first_word= message[0:5]
upper_word= first_word.upper()
new_string= upper_word + message[5:]
print(new_string)

#Exercise 8: Use string interpolation to print out a sentence that contains your number variable.

#Exercise 9: Print “hello world”.
