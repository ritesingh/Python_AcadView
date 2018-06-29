import numpy as np

#Q.1 - Create a numpy array with 10 elements of the shape(10,1) using np.random and find out the mean of the elements using basic numpy functions.
a = np.random.rand(10,1)
print(a)
print("Mean of elements in array: ",np.mean(a))


#Q.2 - Create a numpy array with 20 elements of the shape(20,1) using np.random find the variance and standard deviation of the elements.
b = np.random.rand(20,1)
print(b)
#standard deviation
print("standard deviation of elemrnts in array: ",np.std(b))
#variance
print("variance of elemrnts in array: ",np.var(b))



#Q.3 - Create a numpy array A of shape(10,20) and B of shape (20,25) using np.random. Print the matrix which is the matrix multiplication of A and B. The shape of the new matrix should be (10,25). Using basic numpy math functions only find the sum of all the elements of the new matrix.

c = np.random.rand(10,20)
print(c)
d = np.random.rand(20,25)
print(d)

m = np.dot(c,d)
print("Matrix Multiplication of c and d: \n",m)

print("\n sum of elememts in multiplication array is: ", np.sum(m))



"""Q.4 - Create a numpy array A of shape(10,1).Using the basic operations of the numpy array generate an array of shape(10,1) such that each element is the following function applied on each element of A. 

f(x)=1 / (1 + exp(-x)) 
Apply this function to each element of A and print the new array holding the value the function returns
Example:

a=[a1,a2,a3]   
n(new array to be printed )=[ f(a1), f(a2), f(a3)]"""

A = np.arange(1,11).reshape(10,1)
def fun(x):
    return 1 / (1 + np.exp(-x))

fun = np.vectorize(fun)

new_array = fun(A) 
print("after applyin function to A: \n",new_array)
