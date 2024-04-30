#Timer

import time
import sys

def timer(minutes):
    seconds = 60
    minutes = minutes - 1
    while(True):
        if(seconds == 0 and minutes == 0):
            break
        if(minutes < 10 and seconds < 10):
            sys.stdout.write('\r' + f"0{minutes} : 0{seconds}")
        elif(minutes < 10):
            sys.stdout.write('\r' + f"0{minutes} : {seconds}")
        elif(seconds < 10):
            sys.stdout.write('\r' + f"{minutes} : 0{seconds}")
        else:
            sys.stdout.write('\r' + f"0{minutes} : 0{seconds}")
        if(seconds == 0):
            minutes = minutes - 1
            seconds = 60
        seconds = seconds - 1
        sys.stdout.flush()
        time.sleep(1)

if(__name__ == "__main__"):
    times = int(input("Enter the minutes for timer : "))
    timer(times)



    


