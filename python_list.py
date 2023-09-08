# List Operations with Different Variables and Data

# Create a list of numbers
my_numbers = [10, 20, 30, 40, 50]
my_letters = ['A', 'B', 'C', 'D', 'E']

# Access a value
print(my_letters[1])

# Access the last value
print(my_letters[-1])

# Get the length of the list
print(len(my_letters))

# Append to the list
my_letters.append('F')

# Remove an item from the list
my_letters.remove('C')

# Insert an item into a specific position
my_letters.insert(2, 'X')

# Change a value in the list
my_letters[0] = 'Z'

# Remove an item using pop
my_letters.pop(2)

# Reverse the list
my_letters.reverse()

# Sort the list alphabetically
my_letters.sort()

# Reverse sort the list
my_letters.sort(reverse=True)

# Print the modified list
print(my_letters)
