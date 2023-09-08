# File Operations with Different Variables

# Create a new file and open it for writing
new_file = open('newfile.txt', 'w')

# Get information about the file
print('File Name:', new_file.name)
print('Is Closed:', new_file.closed)
print('Opening Mode:', new_file.mode)

# Write content to the file
new_file.write('This is a new file created with Python.')
new_file.write(' It is so much fun!')
new_file.close()

# Append content to the file
append_file = open('newfile.txt', 'a')
append_file.write(' You can add more content here.')
append_file.close()

# Read content from the file
read_file = open('newfile.txt', 'r+')
file_content = read_file.read(100)
print('File Content (first 100 characters):')
print(file_content)

# Close the file
read_file.close()
