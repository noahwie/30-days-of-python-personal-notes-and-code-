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