# Boolean operators are written with capital F and T
print(True)
print(False)

# Assignment Operators in Python
x = 5 # same as x = 5
x += 3 # same as x = x + 3
x -= 3 # same as x = x - 3
x *= 3 # same as x = x * 3
x /= 3 # same as x = x / 3
x %= 3 # same as x = x % 3
x //=3 # same as x = x // 3 (floor division discard remainder)
x **= 3 # same as x = x ** 3 (exponentation)
x &= 3 # same as x = x & 3
x |= 3 # same as x = x | 3
x ^= 3 #same as x = x ^ 3 (exclusive or bitwise)
x >>= 3 # same as x = x >> 3 (shifts right by 3 bits)
x <<= 3 # same as x = x << 3 (shifts left by 3 bits)

# Arithmetic operators
5 + 3 # Addition
5 - 3 # Subtraction
5 * 3 # Multiplication
5 / 3 # Division
5 % 3 # Modulus
5 ** 3 # Exponentation
5 // 3 # Floor Division

# Example with Integers
print(3 + 5)
print(5 - 3)
print(5 * 3)
print(5 / 3) # Division in Python gives floating numbers
print(5 // 3) # gives Division without floating number or remainder
print(5 % 3) # gives remainder
print(5 * 3) # 5 * 5 * 5

# Example for FLoats
print(3.14) # Pi
print(9.81) # gravity

# Example for Complex Numbers
print(1 + 1j)
print((1 + 1j) * (1 - 1j))

# Comparison Operators
x = 3
y = 5
x == y # Equal
x != y #Not equal
x > y #Greater than
x < y #Less than 
x >= y # greater than or equal to
x <= y # less than or equal to

# Example COmparison Operators 
print(3 > 2) # True 
print(3 >= 2) # True
print(3 < 2) # False
print(3 <= 2) # False
print(3 == 2) #False
print(3 != 2) # True

#in addition to the operators above Python uses is, is not, in, not in operators to compare objects
print(1 is 1) #equals true because data values are the same
print(1 is not 2) #equals true because data values are not the same
print('N' in 'Noah') #true because N is in Noah
print('n' in 'Noah') #False because n is not in Noah only capital N
print('n' not in 'Noah') # True because n is not in Noah

# Logical Operators
# Python also uses keywords and, or, not for logical operators these are used to combine conditional statements
5 < 3 and 8 < 10 #is false altough 8 is smaller than 10, 5 is not smaller than 3 both have to be true 
5 < 3 or 8 < 10 #is true since only one has to be true
not(5 < 3 and 8< 10) # true because not reverses the fals into true 