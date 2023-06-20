import time

seconds = input("Enter the time in seconds : ")

def countDown_timer(seconds):  
    while seconds>0:


        mins = int(seconds/60)
        secs = int(seconds%60)
        timer = f'{mins}:{secs}'
        print(timer)
        seconds -= 1
    print("Timer is up")    

countDown_timer(int(seconds))