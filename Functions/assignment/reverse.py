"""
Write a python program to reverse a string using function
"""
def rev_str(str1):
    str1 = str1[::-1]
    return str1

x = "2234abcd"
print("the original string is: ",x)
print("the reversed string is: ",rev_str(x))

# reverse string
str2 = input("Enter the string:")
def reverse(str2):
    words=str2[::-1]
    print(words)
reverse(str2)