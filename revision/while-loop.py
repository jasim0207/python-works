# reverse of a number using while
# condition rule : we need to decide how many times loop going to work

n = 123  #123/10=Q=12,R=3
rev =0
p =1
s = 0
while n>0:  #12>0 , 1>0
    r = n%10  #3,2,1
    rev=rev*10+r  #3,32,321
    p = p*r
    n = n//10 #12,1
    s = s+r
print('Reverse is:',rev)
print('product is:',p)
print('sum is:',s)

