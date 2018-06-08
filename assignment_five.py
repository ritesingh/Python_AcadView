#Take an input year from user and decide whether it is a leap year or not.
year=int(input("enter any year: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("leap year")
       else:
           print("not a leap year")
   else:
       print("leap year")
else:
   print("not a leap year")

"""Take length and breadth input from user and check whether the dimensions
are of square or rectangle."""
l=int(input("enter length:"))
b=int(input("enter breadth:"))
if(l==b):
    print("taken dim are of square!!")
else:
    print("taken dim are of rectangle!!")


#Take the input age of 3 people and determine oldest and youngest among them.
arr=[]
for i in range(0,3):
    print("enter age of person ",i+1,": ")
    a=int(input())
    arr.append(a)
if(arr[0]<arr[1] and arr[0]<arr[2]):
    print("the youngest among this is :",arr[0])
elif(arr[1]<arr[0] and arr[1]<arr[2]):
   print("the youngest among this is :",arr[1])
else:
   print("the youngest among this is :",arr[2])

if(arr[0]>arr[1] and arr[0]>arr[2]):
    print("the oldest among this is :",arr[0])
elif(arr[1]>arr[0] and arr[1]>arr[2]):
   print("the oldest among this is :",arr[1])
else:
   print("the oldest among this is :",arr[2])


""" Write an if statement that lets a competitor know which of these prizes they won based on the number of points they scored, which is stored in the integer variable points(your input).
points can only take on positive integer values up to 200. If they've won a prize, the message should state "Congratulations! You won a [prize name]!" with the prize name. If there's no prize,
the message should state "Sorry! No prize this time."

Points	Prize
1-50	No Prize
51-150	Wooden Dog
151-180	Book
181-200	Chocolates  """

points=int(input("enter the points of competitor: "))

if points in range(1,51):
    print("Sorry! No prize this time.")
elif points in range(51,151):
    print("Congratulations! You won a Wooden Dog.")
elif points in range(151,181):
    print("Congratulations! You won a Book.")
elif points in range(181,201):
    print("Congratulations! You won Chocolates.")
else:
    print("Invalid Input!!")




"""A shop will give discount of 10% if the cost of
purchased quantity is more than 1000.Ask user for
quantity Suppose, one unit will cost 100. Judge and print total cost for user."""

quant=int(input("enter the quantity of items: "))
if quant*100>1000:
    print("total cost will be:",quant*100-0.1*(quant*100))
else:
    print("total cost will be:",quant*100)
















