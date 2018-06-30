import pandas as pd

#Q.1 - Create a dataframe with your name , age , mail id and phone number and add your friends’s information to the same.
val={'Name':['Ritesh Singh'],'Age':[20],'Email':['gettoriteshsingh@gmail.com'],'ph no.':['9056669767']}
df=pd.DataFrame(val)
df.loc[1]=['Piyush',22,'piyushkp1000@gmail.com','8360434321']
df.loc[2]=['Ajitesh',21,'ajiteshnair@gmail.com','9823477273']
print(df)

"""Q.2 - Download the dataset from this link , 
Click Here
Import the data and print the following :
a.) First 5 rows of Dataframe 
b.) First 10 rows of the Dataframe 
c.) find basic statistics on the particular dataset. 
d.) Find the last 5 rows of the dataframe 
e.) Extract the 2nd column and find basic statistics on it."""

df=pd.read_csv('weather.csv')
print(df.head(5))
print(df.head(10))
print(df['MinTemp'].describe())
print(df['MaxTemp'].describe())
print(df.tail(5))
data=[df.iloc[:,2].sum(),df.iloc[:,2].mean(),df.iloc[:,2].median(),df.iloc[:,2].nunique(),df.iloc[:,2].max(),df.iloc[:,2].min()]
print(data)