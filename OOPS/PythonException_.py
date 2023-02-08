#python Exception
# Exception Handling

try:
    n1 = int(input('Enter first number:'))
    n2 = int(input('Enter 2nd number:'))
    n3 = n1/n2
    print('Output is :',n3)
except Exception as ex:
    print(ex)
# except ZeroDivisionError as er:
#     print(er)
# except ValueError as er:
#     print(er)

