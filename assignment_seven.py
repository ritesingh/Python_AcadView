#Q.1- Create a function to calculate the area of a circle by taking radius from user.
def carea(r):
    return (22/7)*r*r

r=float(input("enter the radius of circle: "))
print("the area of the circle will be: ",carea(r))

"""Q.2- Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a program that determines and prints all the perfect numbers between 1 and 1000. 
[An integer number is said to be “perfect number” if its factors, including 1(but not the number itself), sum to the number. E.g., 6 is a perfect number because 6=1+2+3].
"""
def perfect(n):
    i=1
    sum=0
    while(i<n):
        if n%i==0:
            sum+=i
        i+=1
    if sum==n:
        return " a perfect number"
    else:
        return "not a perfect number"
for i in range(1,1001):
    print(i,"is ",perfect(i))

#Q.3- Print multiplication table of 12 using recursion.
def table(n):
    if n<11:
        print(12,"*",n,"=",12*n)
        n+=1
        return table(n)
    else:
        return "Table printed"
    

print(table(1))  #calling that function 


#Q.4- Write a function to calculate power of a number raised to other ( a^b ) using recursion.
def fact(num):
    if num==0:
        return 1
    else:
        return num*fact(num-1)
        
n=int(input("how many factorial you need to calculate: "))
d=dict()
for i in range(0,n):
    num=int(input("enter the number: "))
    d[num]=fact(num)
print("calculated factorials are: ",d)



