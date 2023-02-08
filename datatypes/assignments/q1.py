#1. Remove empty strings from a list of strings
# str1 = ["John"," ","jack","Emma"," ","jins","Lina"]
# o/p: str1 = ["john","jack","Emma","jins","Lina"]

str1 = ["john","","jack","Emma","","jins","lina"]
i = 0
while i < len(str1):
    if len(str1[i]) == 0:
        str1.pop(i)
    i = i + 1
print(str1)
