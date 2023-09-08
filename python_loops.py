
# Loops and Iterations with Different Variables and Data

# List of names
names = ['Alice', 'Bob', 'Charlie', 'David']

# Simple for loop
for name in names:
    print(f'Hello, {name}!')

# Break statement
for name in names:
    if name == 'Charlie':
        break
    print(f'Hi, {name}!')

# Continue statement
for name in names:
    if name == 'Bob':
        continue
    print(f'Hey, {name}!')



# While loop
count = 0
while count < 5:
    print(f'Count: {count}')
    count += 1
