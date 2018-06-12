#take 10 integers from the user and print on screen
arr=[]
for i in range(0,10):
     a=int(input("enter the ",i+1," number"))
     arr.append(a)
print("the ten numbers are :",arr)


#Write an infinite loop.An infinite loop never ends. Condition is always true.
while(True):
    print("HAHA")



"""Create a list of integer elements by user input. Make a new list which will
store square of elements of previous list."""
arr=[]
siz=int(input("enter the size of list:"))
for i in range(0,siz):
    ele=input("enter the ",i+1," element:")
    arr.append(ele)
print("the original list is",arr)
arr1=[]
for i in arr:
    arr1.append(i*i)
print("the required list is",arr1)


"""From a list containing ints, strings and floats, make three lists to store
them separately"""
arr=[1,2,3,4,'a','b','c',"Ritesh",2.3,5.4,5,6,"SiNgh",4.1]
intarr=[]
strarr=[]
fltarr=[]
for i in arr:
    if isinstance(i,int):
        intarr.append(i)
    elif isinstance(i,str):
        strarr.append(i)
    elif isinstance(i,float):
        fltarr.append(i)
print(intarr,strarr,fltarr,sep="\n")


# Using range(1,101), make a list containing even and odd numbers.

even=[]
odd=[]
for i in range(1,101):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)


"""print the pattern
*
**
***
****
    """
for i in range(0,4):
    for j in range(0,4):
        if i>=j:
            print("*",end="")
    print("\n")
  

#Create a user defined dictionary and get keys corresponding to the value using for loop.
d=dict()
siz=int(input("enter the size of dictionary:"))
for i in range(0,siz):
    k=input("enter key ")
    v=input("enter value ")
    d[k]=v

print("you made the dictionary ",d.items())

ele=input("enter the value whose key is needed:")

for i in d:
    if d[i]==ele:
        print("this is the key:",i)


"""Take inputs from user to make a list. Again take one input from user and search it in the list
and delete that element, if found. Iterate over list using for loop."""
arr=[]
for i in range(0,5):
    a=input("enter the ele:")
    arr.append(a)
b=input("enter the ele to be deleted ")
for i in arr:
    if i==b:
        arr.pop(arr.index(i))
        
print("new array ",arr)





















   
            










        








