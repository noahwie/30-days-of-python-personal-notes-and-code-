# Strings is all text written in single double or tripple quotes.
# Creating a String
letter = 'p' # a string could be a single character or a bunch of texts
print(letter) # prints P
print(len(letter)) # prints 1
greeting = 'Hello World' # you can use single ("") or double quotes ('')
print(greeting)
print(len(greeting)) # len is used to count all characters in a string including whitespace

# Multi line strins are written with triplle single quotes (''') or tripple double quotes (""")
multiline_string = '''This is 
a multi line
String'''
print(multiline_string)

#String concatenation is when single strings get added together with a +
word1 = 'hello'
word2= 'world'
sentence = word1 + word2
print(sentence)

# In Python \ followed by a character is an escape sequence
# \n is a new line
# \t is a tab (8 spaces)
# \\ is a backslash
# \' is a single quote
# \" is a double quote
print('after a backslash \n starts a new line')
print('Days\tTopics\tExcercises') # adding tab space or 4 spaces
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('this is a backslash symbol \\')
print('This is a double quote \"')

# Oldstyle String Formatting with % Operator
# %s String
# %d Integers
# %f Floats
# "%.number of digitsf" Floating point numbers with fixed precision
#Strings only
first_name = 'Noah' 
last_name = 'wieschmann'
language = 'python'
formatted_string = 'I am %s %s. I am learning %s' %(first_name, last_name, language)
print(formatted_string)

# Strings and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formatted_string = 'The area of circle with radius %d is %.2f.' %(radius, area) # 2 refers to the 2 significant digits after the point

python_libraries = ['Django', 'Flask', 'NumPy']
formatted_string2 = 'The following are python libraries:%s' % (python_libraries)
print(formatted_string2)

# New style Formatting (str.format)
first_name
last_name
language
formatted_string3 = 'I am {} {}. I am learning {}' .format(first_name, last_name, language)
print(formatted_string3)

a = 4
b = 3
print('{} + {} = {}' .format(a, b, a+b))

radius
pi
area
formatted_string4 = 'THe area of a circle with a radius {} is {:.2f}' .format(radius, area) # limits to digits after comma
print(formatted_string4)

# String Interpolation / f-Strings (Python 3.6+)
c = 5
d = 6
print(f'{c} + {d} = {c + d}')

# python strings are a sequence of characters and can share methods of access like in lists and tuples
# Unpacking characters
language1 = 'python'
a,b,c,d,e,f = language1 # unpacking sequence characters into variables
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# you can also access single characters of a string by index starting from 0 
first_letter = language1[0]
print(first_letter)
last_index = len(language1) - 1
last_letter = language[last_index]
print(last_letter)

# if starting form right end negative indexing can be used
last_letter = language1[-1]
print(last_letter)

# Strings can be sliced into substrings
language = 'python'
first_three = language[0:3] # starts at index 0 and up to 3 not inlcuding 3
print(first_three) # prints pyt
last_three = language[3:6]
print(last_three) #prints hon
# other ways
last_three = language[-3:] # from last letter -3
print(last_three) # prints hon 
last_three = language[3:] # from index 3 to the end
print(last_three) # prints hon

# reversing a string in python is quite easy
greeting = 'hello world'
print(greeting[::-1])

# characters can also be skipped when slicing strings
language = 'python'
pto = language[0:6:2] # starting from index 0 ending before index 6 skip every 2nd character
print(pto)
