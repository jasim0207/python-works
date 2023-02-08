#table format
dict1 = {"MATHS":87,"SCIENCE":90,"ENGLISH":95,"MALAYALAM":100}
print("SUBJECT\t\t\t\t\tMARKS\n*******************************")
for key,value in dict1.items():
    if key =="MATHS":
        print(key,"\t\t\t\t\t",value)
    else:
        print(key,"\t\t\t\t", value)

 # dictionary to string
dict2 = {"MATHS":87,"SCIENCE":90,"ENGLISH":95,"MALAYALAM":100}
name = "CR7"
print("student name :",name)
for key,value in dict1.items():
    print("the student scored ",value,"mark in subject ",key)

