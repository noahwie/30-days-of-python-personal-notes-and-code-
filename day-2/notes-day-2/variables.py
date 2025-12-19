'''
Variables can be named with A-z, 0-9 and _
standart python variable naming convention is snake_case

'''

# valid variable naming 
firstname
lastname
age
country
city
first_name
last_name
capital_city
_if # since if is a reserved word _ can be used to declare a variable with the name if
year_2021
year2021
current_year_2021
birth_year
num1
num2

# invalid variable names
first-name 
first@name
first$name
num-1
1num

# python is a variable declaration language 
first_name = 'noah'
last_name = 'wieschmann'
country = 'switzerland'
city = 'zurich'
age = '24'
is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Java', 'Python']
person_info = {
    'firstname':'Noah',
    'lastname':'Wieschmann',
    'country':'Switzerland',
    'city':'Zurich'
}

print('hello world') # hello world is the argument passed in the parenthesis
print('hello', 'world') # print can take an unlimited amount of arguments
print(len('hello world')) # len() can only take 1 argument

# printign variables
print('first name: ', first_name)
print('first name length: ', len(first_name))
print('last name: ', last_name)
print('last name length: ', len(last_name))
print('country: ', country)
print('city: ', city)
print('age: ', age)
print('married: ', is_married)
print('skills: ', skills)
print('person information: ', person_info)

# multiple variables can also be declared in one line
first_name, last_name, country, age, is_married = 'noah', 'wieschmann', 'zurich', 24, False
# to assign user input to a variable you need to use input function 
first_name = input('What is your name: ')
age = input('How old are you: ')

print(first_name)
print(last_name)