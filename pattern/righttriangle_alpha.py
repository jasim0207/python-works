n = int(input("enter the levels you want: "))
k = 1
ch = chr(64+k) #getting alphabet

for i in range(n+1):
    for j in range(i):
        print(ch, end=' ') #printing variables
        k += 1
        ch = chr(64 + k) #iterating alphabets
    print()


    