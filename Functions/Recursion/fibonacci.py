# write a code to find fibonacci series using recursion

#function for the nth fibonacci number
def fibo(n):
    if n<0:
        print("Incorrect input")
#1st Fibonnaci number is 0
    elif n == 0:
        return 0
#2nd fibonacci number is 1
    elif n == 1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
#main program
print(fibo(9))