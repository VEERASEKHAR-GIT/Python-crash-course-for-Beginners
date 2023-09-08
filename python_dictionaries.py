# Dictionary Example with Different Variables and Data

# Create a dictionary for a person
employee = {
    'employee_id': 'E12345',
    'first_name': 'Alice',
    'last_name': 'Smith',
    'department': 'Marketing'
}

# Access values
print(employee['first_name'])
print(employee.get('last_name'))

# Add new key-value pair
employee['email'] = 'alice@example.com'

# Get keys
print(employee.keys())

# Get key-value pairs
print(employee.items())

# Create a copy of the dictionary
employee_copy = employee.copy()
employee_copy['position'] = 'Manager'

# Remove items
del employee['department']
employee.pop('email')

# Clear the dictionary
employee.clear()

# Get the length of the copied dictionary
print(len(employee_copy))

# List of dictionaries
employees = [
    {'employee_id': 'E12345', 'first_name': 'Alice', 'last_name': 'Smith'},
    {'employee_id': 'E67890', 'first_name': 'Bob', 'last_name': 'Johnson'}
]

print(employees[1]['last_name'])

