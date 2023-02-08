#Grade and Percentage
m1 = int(input("Enter physics mark: "))
m2 = int(input("Enter chemistry mark: "))
m3 = int(input("Enter biology mark: "))
m4 = int(input("Enter mathematics mark: "))
m5 = int(input("Enter computer mark: "))
percentage = ((m1+m2+m3+m4+m5)*100/500)
print("percentage: ",percentage,"%")

if  percentage>=90:
    print("Grade A")
elif percentage>=80:
    print("Grade B")
elif percentage>=70:
    print("Grade C")
elif percentage>=60:
    print("Grade D")
elif percentage>=50:
    print("Grade E")
elif percentage>=40:
    print("Grade F")
else:
    print("Failed!")



