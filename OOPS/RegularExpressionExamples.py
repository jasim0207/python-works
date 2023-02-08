"""
Regular expressions: it can be used to check if a string contains the specified search pattern
python has a built-in method "re", which can be used to work with regular expression.
#validation - check the user input whether it is valid or not.
client side validation and server side validation
"""
#findall()
import re
# str = 'rose is a beautiful and colourful flower'
# s=re.findall('ful',str)
# print(s)
#
# s1=re.findall('full',str) # if there is no matching in the string returns empty list[].
# print(s1)

# d = 'cat mat pat rat sat '
# #a = re.findall('[sc]',d)
# a = re.findall('[scr]at',d) # [] - set of characters, mention single characters
# print(a)

# d = 'cat mat pat rat sat '
# a = re.findall('[^scr]',d) # ^ except those single characters should not be taken. [^scr]a - scr do not return
# print(a)
#
# d = 'cat mat pat rat sat 99988 999 6666'
# a = re.findall('\d{3}',d) # \d is used for to read digits inside the string
#a = re.findall('\d{3}8',d) # returns ['9998']
#a = re.findall('\d{4}',d) # returns ['9998','6666']

# print(a)
#
# d = 'cat mat pat rat sat 99988 999 6666'
# a = re.findall('\d{1,3}',d)
# print(a)

# d = 'cat mat pat rat sat 99988 999 6666'
# a = re.findall(r'\b\d{4}\b',d)
# print(a)

#search
# str = 'class will start at 10 am'
# s = re.search('\s',str) # first start space position 5
# print(s)
# print(s.start())
#
# s1 = re.search('\d',str) # digit starting position is 20
# print(s1.start())
#
# s2 = re.search('python',str) # if there is no matching object 'None' will return.
# print(s2)

# str = 'class will start at 10pm'
# s = re.search('^class.*10am$',str) # '*' means zero or more occurrences of any characters, '.' means any character in string
# #  '.*' means any characters or more occurrences of any characters  '$'means end with
# print(s)
# if s:
#     print('Find')
# else:
#     print('Not find')

# split()
# str ='class will start at 10am'
# s = re.split(' ',str)
# print(s)
#
# s1 = re.split('a',str)
# print(s1)
#
# s2 = re.split(' ',str,2)
# print(s2)

#fullmatch
# str = 'python is a lang'
# b=re.fullmatch(str,'python is a lang') # fullmatch() compare same order in the string
# print(b)

#sub()
# input= 'rose and jasmine are flowers'
# g=re.sub(' ','*',input) # sub() - substitute '*' in spaces. #rose*and*jasmine*are*flowers
# print(g)
#
# g=re.sub(' ','*',input,3)
# print(g)

#gmail validation using regular expression in python
# import re
#
# regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
#
# def isValid(email):
#     if re.fullmatch(regex, email):
#       print("Valid email")
#     else:
#       print("Invalid email")
# isValid('jas@kk.bb')



# #password validation
# # importing re library
# import re
#
#
# def main():
#     passwd = 'Geek12@'
#     reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
#
#     # compiling regex
#     pat = re.compile(reg)
#
#     # searching regex
#     mat = re.search(pat, passwd)
#
#     # validating conditions
#     if mat:
#         print("Password is valid.")
#     else:
#         print("Password invalid !!")
#
# main()


#validate phone number
# Validate phone number
import re

validate_phone_number_pattern = "^\\+?[1-9][0-9]{7,14}$"
re.match(validate_phone_number_pattern, "+12223334444") # Returns Match object

# Extract phone number from a string
extract_phone_number_pattern = "\\+?[1-9][0-9]{7,14}"
s=re.findall(extract_phone_number_pattern, 'You can reach me out at +12223334444 and +56667778888') # returns ['+12223334444', '+56667778888']
print(s)










