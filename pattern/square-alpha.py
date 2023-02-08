n = 5
for i in range (1,n+1):      #for rows print A to E
    for j in range(1,n+1):    #column
        ch = chr(64+i)      # chr(64+1) print only alphabet A.

        if(i==1 or i==n or j==1 or j==n):
             print(ch, end=" ")
        else:
             print(' ',end=' ')
    print(' ')