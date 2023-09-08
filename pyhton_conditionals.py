# If/Else conditions with different variables and shuffled conditions

a = 25
b = 30

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple if
if a < b:
    print(f'{a} is less than {b}')

# If/else
if a > b:
    print(f'{a} is greater than {b}')
else:
    print(f'{b} is greater than {a}')

# elif
if a < b:
    print(f'{a} is less than {b}')
elif a == b:
    print(f'{a} is equal to {b}')
else:
    print(f'{b} is greater than {a}')

# Nested if
if a > 20:
    if a <= 30:
        print(f'{a} is greater than 20 and less than or equal to 30')

# Logical operators (and, or, not) - Used to combine conditional statements

# and
if a > 20 and a <= 30:
    print(f'{a} is greater than 20 and less than or equal to 30')

# or
if a > 20 or a <= 30:
    print(f'{a} is greater than 20 or less than or equal to 30')

# not
if not(a == b):
    print(f'{a} is not equal to {b}')

# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

numbers_list = [10, 20, 30, 40, 50]

#  in
if a in numbers_list:
    print(f'{a} is in the list')

# not in
if a not in numbers_list:
    print(f'{a} is not in the list')

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is
if a is b:
    print(f'{a} and {b} are the same object')

# is not
if a is not b:
    print(f'{a} and {b} are different objects')
