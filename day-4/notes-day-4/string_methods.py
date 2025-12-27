#python has many built in string methods 

# capitalize()
challenge = 'thirty days of python'
print(challenge.capitalize()) # capitalizes first character of a string

#count() returns occurences in a string. count(substring, start index, end index)
challenge = 'thirty days of python'
print(challenge.count('y')) # occurs three times
print(challenge.count('y', 7, 14)) # how many times does y occur from index 7 to 14
print(challenge.count('th')) # substring occurs 2 times

# endswith() checks if a string ends with a specified ending returns true or false
challenge = 'thirty days of python'
print(challenge.endswith('on')) # True
print(challenge.endswith('tion')) # False

# expandtabs() replaces tab character with spaces default tab size is 8. it takes tab size arguments
challenge1 = 'thirty\tdays\tof\tpython'
print(challenge1.expandtabs())
print(challenge1.expandtabs(10))

# find() returns the index of the first occurence of a substring if not found it returns -1
challenge = 'thirty days of python'
print(challenge.find('y')) # 5
print(challenge.find('th'))
print(challenge.find('abc'))

# rfind() returns index of the last occurence of a substring if not found retunrs -1
challenge = 'thirty days of python'
print(challenge.rfind('y')) #16
print(challenge.rfind('th')) #17

# format(): formats strings into a nicer output
first_name = 'Noah'
last_name = 'Wieschmann'
age = 24
job = 'developer'
country = 'switzerland'
sentence = 'I am {} {}. I am a {}. Iam {} years old. I live in {}'.format(first_name, last_name, age, job, country)
print(sentence) # I am Noah Wieschmann. I am a 24. Iam developer years old. I live in switzerland

# index() returns the lowest index of a substring. Additional arguments indicate starting and ending index (default 0 and string length -1)
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string)) # 7
print(challenge.index(sub_string, 9)) # error

# rindex() returns the highest index of a substring. additional arguments indicate starting and ending index (default 0 and string length -1)
print(challenge.rindex(sub_string)) # 7
print(challenge.rindex(sub_string, 9)) # error
print(challenge.rindex('on', 8)) # 19

# isalnum(): checks alphanumeric character
challenge_1 = 'thirtydaysofpython'
print(challenge_1.isalnum()) # true
print(challenge.isalnum()) # false spaces are not alphanumeric characters

# isalpha() checks if all characters are alphabetical charachters (a-z and A-Z)
print(challenge.isalpha()) # false, space again is not a alphabetical character
print(challenge_1.isalpha()) # true
num = '123'
print(num.isalpha()) # false

# isdecimal() checks if all characters in a string are decimal (0-9)
print(challenge.isdecimal()) # false
print(num.isdecimal()) # true
#space again is not a decimal

# isdigit() checks if all characters in a string are numbers same as isdecimal() but some unicode numbers are included

# isidentifier() checks if a string is a valid identifier (valid variable name) 
# 30DaysOfPython -> false since variables cant start with numbers
# thirtyDaysOfPython -> true

# islower() checks if all alphabet characters are lowercase

# isupper() checks if all alphabet characters are uppercase

# join() returns concatenated string
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ''.join(web_tech)
print(result) # 'HTML CSS JavaScript React?

# replace() replaces substring with a given string
greeting = 'happy christmas'
print(greeting.replace('christmas', 'holidays')) # 'happy holidays

# split() splits a string using given string or space as a separator
challenge = 'thirty days of pythin'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']

# title() returns a title cased string
title = 'this is a title'
print(title.title()) # This Is A Title

# swapcase() converts all uppercase characters to lowercase and all lowercas to uppercase characters
challenge = 'This Is Thirty Days Of Python'
print(challenge.swapcase()) # tHIS iS tHIRTY dAYS oF pYTHON

# startswith() checks if a string starts with the specified string
challenge
print(challenge.startswith('thirty')) # true

