year = int(input("Enter the year: "))
# divided by 100 means centuary year (ending with 00)
# centuary year divided by 400 is leap year
if (year%400==0) and (year % 100 == 0):
    print(year,"is leap year")

# not divided by 100 means not a centuary year
# year divided by 4 is a 4 is a leap year

elif (year % 4 == 0) and (year % 100!=0):
    print(year,"is a leap year")

else:
    print(year,"is not a leap year")


