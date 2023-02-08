#for loop
fruit = "banana"
for i in fruit:
    print(i)
# i check for all charachters i = b, i = a, i = n etc.

fruit1 = "apple"
for letter in fruit1:
    print(letter)
#find method
a = "orange"
b = a.find("ge")
print(b)

c = a.find("z") #if substring is not found find() returs -1.
print(c)
#replace
greet = "Hello bob"
nstr = greet.replace('bob','jane')#name replacing
print(nstr)

nstr = greet.replace('o','X')#letter replacing
print(nstr)
