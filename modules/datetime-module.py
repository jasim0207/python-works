import datetime

now = datetime.datetime.now() # representing a single point in time including date and time
crnt_date = datetime.date.today() # print the current date (2023-01-03)-(yy-mm-dd) without time
print(crnt_date)
print(now)
print(dir(datetime))