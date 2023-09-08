# custom_email_validation.py

import re

def custom_validate_email(email_address):
    if len(email_address) > 7:
        return bool(re.match(r"^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email_address))
