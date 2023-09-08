# Tuples in Python are ordered and unchangeable collections that allow duplicate members.

# Create a tuple
colors_tuple = ('Red', 'Green', 'Blue')

# Using a constructor
# colors2 = tuple(('Red', 'Green', 'Blue'))

# A single value tuple needs a trailing comma
single_color_tuple = ('Red',)

# Access a value
print(colors_tuple[1])

# You can't change the value of a tuple - it's immutable
# colors_tuple[0] = 'Yellow'  # This will result in an error

# Delete a tuple
del single_color_tuple

# Get the length of the tuple
print(len(colors_tuple))

# Sets in Python are unordered and unindexed collections with no duplicate members.

# Create a set
colors_set = {'Red', 'Green', 'Yellow'}

# Check if an element is in the set
print('Red' in colors_set)

# Add an element to the set
colors_set.add('Blue')

# Remove an element from the set
colors_set.remove('Blue')

# Adding a duplicate element has no effect
colors_set.add('Red')

# Clear the set
colors_set.clear()

# Delete the set
del colors_set

# The set will no longer exist after deletion
# print(colors_set)  # This will result in an error since the set is deleted
