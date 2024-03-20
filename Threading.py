import threading
import time

def update_db():
    print("updating db.....")
    time.sleep(5)
    print("Updated db")

def display_num(num):
    for i in range(1,num+1):
        print(i)

thread1=threading.Thread(target=update_db)
thread1.start()

display_num(10)

thread1.join()
print("BYE")
#print(threading.active_count())
#print(threading.enumerate())
