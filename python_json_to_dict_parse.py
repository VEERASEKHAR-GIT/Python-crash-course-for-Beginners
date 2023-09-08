# Import the JSON module
import json

# Sample JSON data
person_data_json = '{"first_name": "Alice", "last_name": "Smith", "age": 25}'

# Parse JSON into a Python dictionary
person_data = json.loads(person_data_json)

# Access and print values from the dictionary
# print(person_data)
# print(person_data['first_name'])

# Create a Python dictionary
vehicle = {'make': 'Toyota', 'model': 'Camry', 'year': 2020}

# Convert the dictionary to JSON format
vehicle_json = json.dumps(vehicle)

# Print the JSON data
print(vehicle_json)
