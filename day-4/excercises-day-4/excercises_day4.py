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
