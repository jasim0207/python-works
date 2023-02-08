#2. write a python code to remove all the repeating letters from a each words of a given sentence.
# i/p: let's google the pineapple
# o/p: let's gole the pineal


str = "let's google the pineapple"
str1 = str.split(' ')
str2 =[]
#print(str2)
for i in str1: #let's, google, the, pineapple
    #print(i)
    l = ""
    for j in i: #l, e, t, ',s g,
        #print(j)
        if j in l:
            continue
        else:
            l = l+j
            #print(l)
    str2.append(l)
print(' '.join(str2))