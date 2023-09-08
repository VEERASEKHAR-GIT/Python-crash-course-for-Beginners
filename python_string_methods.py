# Strings in Python can be enclosed in single or double quotation marks. Let's explore string formatting and various string methods.

my_name = 'Alice'
my_age = 25

# String Concatenation
print('Hello, my name is ' + my_name + ' and I am ' + str(my_age) + ' years old.')

# String Formatting

# Using arguments by position
print('My name is {name} and I am {age} years old.'.format(name=my_name, age=my_age))

# Using F-Strings (Python 3.6+)
print(f'Hello, my name is {my_name} and I am {my_age} years old.')

# String Methods

text = 'helloworld'

# Capitalize the string
print(text.capitalize())

# Convert to all uppercase
print(text.upper())

# Convert to all lowercase
print(text.lower())

# Swap case of characters
print(text.swapcase())

# Get the length of the string
print(len(text))

# Replace a substring
print(text.replace('world', 'everyone'))

# Count occurrences of a substring
substring = 'l'
print(text.count(substring))

# Check if the string starts with a particular substring
print(text.startswith('hello'))

# Check if the string ends with a particular substring
print(text.endswith('d'))

# Split the string into a list
print(text.split())

# Find the position of a substring
print(text.find('r'))

# Check if the string is alphanumeric
print(text.isalnum())

# Check if the string contains only alphabetic characters
print(text.isalpha())

# Check if the string contains only numeric characters
print(text.isnumeric())

# Check if the string is in titlecase (words start with uppercase)
print(text.istitle())

# Strip leading and trailing whitespace
whitespace_text = '   Hello, World!   '
print(whitespace_text.strip())

# Check if the string is in lowercase
lowercase_text = 'hello'
print(lowercase_text.islower())

# Check if the string is in uppercase
uppercase_text = 'WORLD'
print(uppercase_text.isupper())

# Check if the string is a valid identifier
identifier = 'my_variable123'
print(identifier.isidentifier())
