# calculates time left in seconds if you live until a hundred
age = int(input('how old are you?'))
time_left = 3153600000 - (age * 31556952)
print('if you live to 100 years old you have', time_left, 'seconds left  to live')