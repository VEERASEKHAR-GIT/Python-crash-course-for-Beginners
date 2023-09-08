# Importing Core Modules with Different Variable Names
import datetime as dt  # Importing 'datetime' module as 'dt' for date and time functionality
from datetime import date as today_date  # Importing 'date' class as 'today_date' from 'datetime'

import time as tm  # Importing 'time' module as 'tm' for time-related functions
from time import time as current_time  # Importing 'time' function as 'current_time' from 'time'

# Importing a Module Installed via pip
from camelcase import CamelCase as CC  # Importing 'CamelCase' class as 'CC' from 'camelcase' module

# Importing a Custom Module
import validator as val  # Importing a custom module named 'validator' as 'val'
from validator import validate_email as is_valid_email  # Importing 'validate_email' function as 'is_valid_email'

# Using Core Modules
current_date = today_date.today()  # Get the current date using 'today_date'
current_timestamp = current_time()  # Get the current timestamp using 'current_time'

# Using the CamelCase module
cc_instance = CC()
# camelcased_text = cc_instance.hump('hello there world')  # Convert a string to CamelCase (commented out for simplicity)

# Using the custom 'validator' module to check email validity
test_email = 'test#test.com'
if is_valid_email(test_email):
    print('Email is valid')
else:
    print('Email is not valid')

