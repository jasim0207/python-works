# write a program to find the sum of natural numbers using recursion.

def getsum(num):
    if num == 1:
      return 1
    print(num)
    print(num + getsum(num - 1))
    return num + getsum(num-1)
num = 10
print(getsum(num))
