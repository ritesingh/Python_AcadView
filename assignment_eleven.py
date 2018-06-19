import threading 
import time

#Q1. Create a threading process such that it sleeps for 5 seconds and then prints out a message.
def for_5_sec():
    print(threading.currentThread().getName(),'Starting')
    time.sleep(5)
    print('I waked up after 5 seconds now let me die again')

t=threading.Thread(name="for_5_sec",target=for_5_sec)
t.start()

#Q2. Make a thread that prints numbers from 1-10, waits for 1 sec between.
def sec_ques():
    for i in range(1,11):
       print(threading.currentThread().getName(),i)
       time.sleep(1)

t=threading.Thread(name="thread is printing:",target=sec_ques)
t.start()

"""Q3. Make a list that has 5 elements.Create a threading process that prints the 5 elements of the list with a 
delay of multiple of 2 sec between each display. Delay goes like 2sec-4sec-6sec-8sec-10sec"""
def delay_print():
    arr=[1,2,3,4,5]
    j=2
    for i in arr:
        print(threading.currentThread().getName(),i)
        time.sleep(j)
        j+=2
    

t=threading.Thread(name="array element after 2*n seconds::",target=delay_print)
t.start()


#Q4. Call factorial function using thread.
def factorial(n):
    fact=1
    for i in range(n,0,-1):
        fact*=i
    print(threading.currentThread().getName(),fact)


n=int(input("which number do you want to calc factorial for "))
t=threading.Thread(name="factorial thread gave me: ",target=factorial,args=(n,))
t.start()



