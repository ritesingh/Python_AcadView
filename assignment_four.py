import operator 

#Write a program to create a tuple with different data types and do the following operations. 
 #Find the length of tuple
t=(1,2,[3,4,5,6],'d','e','f','j')
print("tuple is ",t)
print("length of tuple is ",len(t))

"""Find the largest and smallest element of the tuple, we cannot find largest and smallest element until 
  tuple consist single data ty"""
tu=(4,2,19,54,20,56,32,11,99)
print("maximum element in tuple ",tu," is ",max(tu))
print("minimum element in tuple ",tu," is ",min(tu))

 #to find the product of all elements of a tuple
pro=1
for i in tu:
     pro=pro*i 
print("product of all elements of tuple ",tu," is: ",pro)


#Q.1- Create two set using user defined values.
s1=set([])
s2=set([])
size=int(input("Enter the size of set1: "))
size1=int(input("Enter the size of set2: "))
print("input set 1: ")
for i in range(0,size):
      a=input()
      s1.add(a)
print("input set 2: ")
for i in range(0,size1):
      a=input()
      s2.add(a)
print("Set 1 is: ",s1)
print("Set 2 is: ",s2)

 #difference between two sets
s3=s1-s2
print("difference is: ",s3)
 
 #compare two sets 
print("whether s1 is subset of s2: ",s1<=s2)
print("whether s2 is subset of s1: ",s2<=s1)
print("whether s1 is same as of s2: ",s1==s2)
 
 #intersection of two sets 
print("intersection of s1 and s2:",s1&s2)


#Q.1- Create a dictionary to store name and marks of 10 students by user input.
d=dict()
for i in range(0,10):
    print("enter name of student",i+1,": ")
    name=input()
    marks=int(input("enter marks for him: "))
    d[name]=marks
print("the created dictionary with count is: ",d)

#Sort the above dictionary according to marks
 #as dict are unsortable we can only represent it in sortable form and i have used list of tuples to do so.
sort = sorted(d.items(), key=operator.itemgetter(1))
print("sorted dictionary is: ",sort)

#Count the number of occurrence of each letter in word "MISSISSIPPI". Store count of every letter with the letter in a dictionary.
s="MISSISSIPPI"
d1=dict((letter,s.count(letter)) for letter in set(s))
print("required dictionary is: ",d1)


