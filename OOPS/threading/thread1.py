#python thread

# from time import sleep
# def task():
#     # block for a moment
#     sleep(3) # sleep() wait 3 seconds to display output
#     # display message
#     print('this is another thread')
#
# #task()
#
# from threading import Thread
# # create a thread
# thread = Thread(target=task) # here thread is an object
# #Next, we can create an instance of the threading. thread class and specify
# # our function name as the "target" argument in the constructor.
# # run the thread
#
# thread.start()

# the start() function does not block, meaning it returns immediately.



from time import sleep
from threading import Thread

# a custom function that blocks for a moment
def task(sleep_time, message):
    # block for a moment
    sleep(sleep_time)
    # display a message
    print(message)
#create a thread
thread = Thread(target=task, args=(1.5, 'New message from another thread'))
# run the thread
thread.start()
# wait for the thread to finish
print('waiting for the thread')


import time
import threading

def cal_sqre(num): # define the cal_sqre function
    print("calculate the square root of the given number")
    for n in num:
        time.sleep(0.3) #at each iteration it waits for 0.3 time
        print('Square is : ', n * n)
def cal_cube(num): # define the cal_cube() function
    print("Calculate the cube of the given number")
    for n in num:
        time.sleep(0.3) # at each iteration it waits for 0.3 time
        print("cube is : ", n * n * n)
arr = [4, 5, 6, 7, 2] #given array

t1 = time.time() #get total time to execute the function
# cal_sqre(arr) # call cal_sqre() function
# cal_cube(arr) # call cal_cube() function

th1 = threading.Thread(target=cal_sqre, args=(arr,))
th2 = threading.Thread(target=cal_cube, args=(arr, ))
th1.start()
th2.start()
th1.join()
th2.join()
print("Total time taken by thread is : ",time.time() - t1) #print the total time
