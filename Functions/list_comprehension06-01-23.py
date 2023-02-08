print([x for x in "hello world"])
#for i in "hello world":
#   print(i)

#ex - multiple conditions (list comprehension)
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0 ]
print(num_list)

# multiple loops
prime = [x for x in range(2,21) if all(x%y!= 0 for y in range(2,x))]

print(prime)

#ex-2
h_letters = []
for letter in 'human':
    h_letters.append(letter)
print(h_letters)

#ex-2 list comprehension

h_letters = [letter for letter in "human"]
print(h_letters)

# even
even = [x for x in range(101) if x%2==0]
print(even)
#odd
odd = [y for y in range(101) if y%2!=0]
print(odd)

# sum of n natural numbers
print(sum([i for i in range(13)]))
print(sum([j for j in range(1, int(input("enter the range :"))+1)]))
#equation
print([(n*(n+1)/2) for n in range(1, int(input("enter the range :"))+1)])


