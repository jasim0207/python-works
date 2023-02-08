# a e i o u , A E I O U
#check for vowels
vowels = ['a','e','i','o','u','A','E','I','O','U']
a = input("enter the alpahabet")
for i in a:
    if i in vowels:
        print(f' {i} is vowel')
    else:
        print(f'{i} is consonant')
