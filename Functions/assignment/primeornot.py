"""check whether the given number is prime or not using function"""

def prime(Number):
    count = 0
    i = 2
    while(i<=Number//2):
        if(Number % i== 0):
            count = count+1
            break
        i = i+1
    if(count==0 and Number !=1):
        print("%d is a prime number" %Number)
    else:
        print("%d is not prime number" %Number)

Number = int(input("Enter num: "))
prime(Number)
