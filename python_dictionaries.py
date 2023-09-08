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

