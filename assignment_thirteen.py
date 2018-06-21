"""Q.1- Name and handle the exception occured in the following program: 

a=3
 if a<4:
    a=a/(a-3)
     print(a)"""
a=3
if a<4 :
    try:
        a = a/(a-3)

    except ZeroDivisionError:
        print("Zero se divide kar diye bhai , dhyan do")

    else:
        print("Everything cool:")
        print(a)

"""Q.2- Name and handle the exception occurred in the following program: 
l=[1,2,3]
print(l[3])"""
l=[1,2,3]

try:
    print(l[3])
    
except IndexError:
    print("jitna kambal hai utna pair failaao!!")

"""Q.3- What will be the output of the following code:

# Program to depict Raising Exception
 
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print "An exception"
    raise  # To determine whether the exception was raised or not
"""
try:
    raise NameError("hello")  # Raise Error displaying Hi there

except NameError:
    print("An exception")


