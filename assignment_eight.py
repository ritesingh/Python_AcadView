import time
import math
import os
#Q.1- What is Time Tuple?
print("ANS:- In the module time the tuple returned by localtime and gmtime containing (year, month, day, hour, minute, second, day of week, day of year, daylight savings flag)  where the year number is four digits, the day of week begins with 0 for Monday, and January 1st is day number 1 is called time tuple.")



#Q.2- Write a program to get formatted time.
print("formatted local current time :",time.ctime())


#Q.3- Extract month from the time.
print("the extracted month is ",time.ctime()[4:7])

#Q.4- Extract day from the time.
print("the day is ",time.ctime()[0:3])

#Q.5- Extract date (ex : 11 in 11/01/2021) from the time.
print("the extracted date is ",time.ctime()[8:10])

#Q.6- Write a program to print time using localtime method.
localtime = time.localtime(time.time())
print("time using localtime ",localtime," method is: ",localtime[3:6])

#Q.7- Find the factorial of a number input by user using math package functions.
num = int(input("Enter number: "))
print("factorial using math module is: ",math.factorial(num))

#Q.8- Find the GCD of a number input by user using math package functions.
print("******TO FIND GCD********")
a=int(input("enter first num: "))
b=int(input("enter second num: "))
print("GCD is : ",math.gcd(a,b))

#Q.9- Use OS package and do the following tasks: 
#1. Get current working directory.
print("current working directory is: ",os.getcwd())
#2. Get the user environment.
print("the user environment is: ",os.environ["HOMEPATH"])


