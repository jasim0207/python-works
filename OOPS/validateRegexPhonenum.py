# Validate phone number
import re

validate_phone_number_pattern = "^\\+?[1-9][0-9]{7,14}$"
re.match(validate_phone_number_pattern, "+12223334444") # Returns Match object

# Extract phone number from a string
extract_phone_number_pattern = "\\+?[1-9][0-9]{7,14}"
s=re.findall(extract_phone_number_pattern, 'You can reach me out at +12223334444 and +56667778888') # returns ['+12223334444', '+56667778888']
print(s)