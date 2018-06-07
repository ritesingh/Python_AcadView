
#a list with user defined inputs
a=[]
size=int(input("Enter the size of List:"))
for i in range(0,size):
    inp=input("enter element ")
    a.append(inp)
print("your list is :",a)

#add the following to the above list
b=["google","apple","facebook","microsoft","tesla"]
a=a+b
print("your appended list is :",a)

#count the number of items an object occurs
for i in a:
    print("element ",i," occurs ",a.count(i)," times in the list.")

#create a list with numbers and sort it in asc order
c=[3,2,5,7,3,5,10,98,54,22]
print("\nthe sorted list will be ",sorted(c))

"""Given are two one-dimensional arrays A and B which are sorted in 
ascending order. Write a program to merge them into a single sorted 
array C that contains every item from arrays A and B, in ascending order. [List] """
A=[1,7,23,25,35,36]
B=[1,2,3,4,5,6]
C=A+B
print("\nAfter adding both the lists the final sorted list is ",sorted(C))

#implement stack and queue using list
A=[1,7,23,25,35,36]
    #Stack Last in First Out
A.append(2)
print("added 2 ",A)
A.append(1)
print("added 1 ",A)
A.pop()
print("Stack implemented popping here from last ",A)
    #Queue First In First Out i am importing for this 
A=[1,7,23,25,35,36]
A.append(1)
print("added 1 ",A)
A.append(0)
print("added 0 ",A)
A.pop(0)
print("Queue Implemented popping from left ",A)



#Count even and odd numbers in a list
even=0
odd=0
for i in A:
    if(i%2==0):
        even+=1
    else:
        odd+=1
print("count of even numbers ",even)
print("count of odd numbers ",odd)        





