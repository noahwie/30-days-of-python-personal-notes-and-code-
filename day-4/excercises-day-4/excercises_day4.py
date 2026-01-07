# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
words = ['Thirty', 'Days', 'Of', 'Python']
sentence = ' '.join(words)
print(sentence)

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
words1 = ['Coding', 'For', 'All']
sentence1 = ' '.join(words1)
print(sentence1)

# Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'

# Print the variable company using print().
print(company)

# Print the length of the company string using len() method and print().
print(len(company))

# Change all the characters to uppercase letters using upper() method.
print(company.upper())

# Change all the characters to lowercase letters using lower() method.
print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Cut(slice) out the first word of Coding For All string.
print(company[7:])

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find('All'))

# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))

# Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
company1 = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(company1.split(','))

# What is the character at index 0 in the string Coding For All.
print(company[0])

# What is the last index of the string Coding For All.
print(company[-1])

# What character is at index 10 in "Coding For All" string.
print(company[10])

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
sentence = 'Python For All'
abbreviation = ''.join(word[0] for word in sentence.split())
print(abbreviation)

# Create an acronym or an abbreviation for the name 'Coding For All'
sentence = 'Coding For All'
abbreviation = ''.join(word[0] for word in sentence.split())
print(abbreviation)

# Use index to determine the position of the first occurrence of C in Coding For All.
sentence = 'Coding For All'
print(sentence.index('C'))

# Use index to determine the position of the first occurrence of F in Coding For All.
sentence = 'Coding For All'
print(sentence.index('F'))

#Use rfind to determine the position of the last occurrence of l in Coding For All People.
sentence = 'Coding For All'
print(sentence.rfind('l'))

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
first_occurence = sentence.index('because')
print(first_occurence)

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
last_occurence = sentence.rindex('because')
print(last_occurence)

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
sliced_sentence = sentence[31:54]
print(sliced_sentence)

# Does ''Coding For All' start with a substring Coding?
sentence = 'Coding For All'
print(sentence.startswith('Coding'))

# Does 'Coding For All' end with a substring coding?
sentence = 'Coding For All'
print(sentence.endswith('coding'))

# '     Coding For All      '  , remove the left and right trailing spaces in the given string.
sentence = '   Coding For All      '
new_sentence = sentence.strip('     ')
print(new_sentence)

# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
string1 = '30DaysOfPython'
string2 = 'thrity_days_of_python'
print(string1.isidentifier())
print(string2.isidentifier())

#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(libraries))

# Use the new line escape sequence to separate the following sentences.
#I am enjoying this challenge.
#I just wonder what is next.
print('I am enjoying this challenge.\nI just wonder what is next.')

#Use a tab escape sequence to write the following lines.
#Name      Age     Country   City
#Asabeneh  250     Finland   Helsinki
print('Name\tAge\tCountry\tCity')
print('Asabaneh\t250\tFinland\tHelsinki')

# Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {} meters square'.format(radius, area))

#Make the following using string formatting methods:
a = 8
b = 6

print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))