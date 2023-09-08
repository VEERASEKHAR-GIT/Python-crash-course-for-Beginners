# main.py

# Import the custom_email_validation module
import custom_email_validation

# Use the custom_validate_email function from the module
email = 'test@example.com'
if custom_email_validation.custom_validate_email(email):
    print('Email is valid')
else:
    print('Email is not valid')
