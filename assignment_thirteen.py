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

Program to depict Raising Exception
 
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print "An exception"
    raise  # To determine whether the exception was raised or not
"""
print("OUTPUT WILL BE ->An exception")



"""
Q.4- What will be the output of the following code:

 # Function which returns a/b
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print "a/b result in 0"
	else:
		print c

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)"""

print("-5.0\na/b result in 0")
print("when a=2.0 and b=3.0 their difference is not zero and thus they execute normally which is not the case with a=3.0 and b =3.0")


"""
Q.5- Write a program to show and handle following exceptions: 
1. Import Error
2. Value Error
3. Index Error
"""
try:
    import lapata

except ImportError:                             
    print("Import/export ka business hai kya? ye python hai!")     
else:
    print("u r smart !")
try:
    y = int(input("Enter number:"))
    
except ValueError:
    print("padh to lete manga kya tha.. ValueError jhelo ab")

else:
    print("Cool u r smart!")

try:
    arr=[1,2,3,4]
    print(arr[5])

except IndexError:
    print("Kaha na kambal dekh k pair failaao! Jhelo IndexError")


"""
Q.6- Create a user-defined exception AgeTooSmallError() that warns the user when they have entered age less than 18. 
The code must keep taking input till the user enters the appropriate age number(less than 18). """
class AgeTooSmallError(Exception):          #class for the custom error
    print("naabaaliko k liye khed hai!")
def trying():
    try:
        age = int(input("Enter age:"))
        if age<18:
            raise AgeTooSmallError              #raises the error we defined

    except AgeTooSmallError:
        if age<18 :
            print("ERROR, enter age above 18 ") #keep entering until done        
            trying()
    else:
        print("now you can proceed!!")
trying()


