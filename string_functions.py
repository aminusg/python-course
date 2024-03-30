# sentence = 'The quick brown fox jumped'
# sentence -> variable
# 'The quick brown fox jumped' -> string
# = -> assignment


""" PYTHON DOCUMENTATION
    str.upper()
    Return a copy of the string with all the cased characters [4] converted to uppercase. Note that s.upper().isupper() might be False > if s contains uncased characters or if the Unicode category of the resulting character(s) is not “Lu” (Letter, uppercase), but e.g. > “Lt” (Letter, titlecase).

    str.capitalize()
    Return a copy of the string with its first character capitalized and the rest lowercased.

    str.lower()
    Return a copy of the string with all the cased characters [4] converted to lowercase. """


sentence = 'The quick brown fox jumped'
sentence_two = sentence.upper()

print(sentence)
print(sentence_two)

sentence = 'the quick brown fox jumped'.capitalize()
print(sentence)

sentence = 'the quick brown fox jumped'.title()
print(sentence)

sentence = 'the Quick Brown fOx jumped'
print(sentence.lower())


#Python is a zero based numbering system

#RANGES
# The quick brown fox jumped
# T => 0
# h => 1
# e => 2
# ' ' => 3

starter_sentence = 'The quick brown fox jumped'

new_sentence = 'Thy' + starter_sentence[3:]

print(new_sentence)