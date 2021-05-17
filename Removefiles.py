import time
import shutil
import os

# Making a variable of path
path = 'C:\\Users\\Dhairya\\Desktop\\bla.txt'

# Creating a function for getting the time for the path and converting it into days
def time():
    cTime = os.stat(path).st_ctime
    seconds = cTime//1000
    minutes = seconds//60
    hours = minutes//60
    days = hours//24
    time = days

    return time

def remove():
    time1 = time()
    if(time1 <= 30.0):
        os.remove(path)
    else:
        b = 0

remove()
