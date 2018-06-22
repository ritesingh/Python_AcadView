import random


#Q.2- Write a Python program to count the frequency of words in a file.
arr= []
with open("test1.txt",'r',encoding='utf-8') as fp:   #i am applying utf as it was not working without it on my pc.
    stuff = fp.readlines() 
    for line in stuff: 
        words=line.split()
        arr+=words
fp.close()
ele= input("Whose frequency to find? ")

print("%s has a frequency of:%d"%(ele,arr.count(ele)))

#Q.3- Write a Python program to copy the contents of a file to another file.
#copyfile('test.txt','newtest.txt')  #this is a python inbuilt function from shutil module. but still i am doing it this way:
with open('test1.txt', 'r',encoding='utf-8') as f1, open('newtest1.txt', 'w',encoding='utf-8') as f2:
    for line in f1:
        f2.write(line)
f1.close()
f2.close()

#Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.
with open('test1.txt','r',encoding='utf-8') as fh1, open('newtest1.txt','r',encoding='utf-8') as fh2:
    for line1, line2 in zip(fh1, fh2):
        # line1 from test1.txt, line2 from newtest1.txt
        print(line1+line2)   

fh1.close()
fh2.close()


#Q.5- Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.
arr=[]
f = open("Random.txt","w",encoding='utf-8' )

for i in range(int(input('How many random numbers?: '))):
    line = str(random.randint(1, 1000))
    f.write(line+'\n')

f.close()

with open("Random.txt",'r',encoding='utf-8') as f:
    stuff = f.readlines() 
    for line in stuff: 
        print(line)
        arr.append(line)

arr.sort()

f.close()

with open("SortedRand.txt",'w',encoding='utf-8') as f1:
    for i in arr:
        f1.write(i)   #copies to SortedRand in a sorted form