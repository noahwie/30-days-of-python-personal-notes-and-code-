# Day 2: 30 Days of python programming
first_name = 'noah'
last_name = 'wieschmann'
full_name = 'noah wieschmann'
country = 'switzerland'
city = 'zurich'
age = 24
year = 2025
is_married = False
is_true = True
is_light_on = True
variable1, variable2, variable3 = 1, 2, 3
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(len(first_name))
print(first_name == last_name)
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two
#radius = 30
# area_of_circle = 3.14 * (radius * radius)
# circum_of_circle = (2 * radius) * 3.14
radius = int(input('type in the radius of your circle: '))
area_of_circle = 3.14 * radius * radius
circum_of_circle = 2 * radius * 3.14
print(area_of_circle)
print(circum_of_circle)

name = input('what is your first name?')
last_name = input('what is you last name?')
country = input('what country do you come from?')
age = input('how old are you?')
print(name, last_name, country, age)
