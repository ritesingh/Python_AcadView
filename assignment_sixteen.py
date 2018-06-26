import mysql.connector as pm
import sqlite3
"""Q.1- Create a database. Create the following tables:
1. Book
2. Titles
3. Publishers
4. Zipcodes
5. AuthorsTitles
6. Authors
Refer to the diagram below"""

try:
con = pm.connect(host='localhost', database='riteshdb', user='root', password='ritesh123')
cursor = con.cursor()
query6 = 'Create table Authors(AuthorID int primary key,FirstName varchar(15),MiddleName varchar(15),LastName varchar(15))'
cursor.execute(query6)
query4 = 'Create table Zip_Codes(Zip_Code_ID int primary key,City varchar(15),State varchar(20),Zip_Code int)'
cursor.execute(query4)
query3 = 'Create table Publishers(Publisher_ID int primary key,Name varchar(15),Street_Address varchar(50),Suite_Number int,Zip_Code_ID int,foreign key(Zip_Code_ID) references Zip_Codes(Zip_Code_ID))'
cursor.execute(query3)
query2 = 'Create table Titles(TitleId int primary key,Title varchar(35),ISBN int,Publisher_ID int,Publication_Year int,foreign key(Publisher_ID) references Publishers(Publisher_ID))'
cursor.execute(query2)
query1 = 'Create table Books(BookId int primary key,TitleId int,Location varchar(15),Genre varchar(10),foreign key(TitleId) references Titles(TitleId))'
cursor.execute(query1)
query5 = 'Create table Authors_Titles(Author_Title_ID int primary key,AuthorID int ,TitleId int,foreign key(AuthorID) references Authors(AuthorID),foreign key(TitleId) references Titles(TitleId))'
cursor.execute(query5)
print('Table Created')
except pm.DatabaseError as e:
  if con:
    con.rollback()
  print('Problem occured: ', e)
finally:
  if cursor:
    cursor.close()
  if con:
    con.close()

#Q.2- Insert values in the tables.
conn=sqlite3.connect("riteshdb.db")
cur=conn.cursor()
a='insert into AuthorsTitles values("RA141","MANSIME",12345);'
cur.execute(a)
a='insert into AuthorsTitles values("RA141","MANSIME",78900);'
cur.execute(a)
b='insert into Authors values("MANSIME","mansi","kumar","mehta");'
cur.execute(b)
c='insert into Titles values(3102,123456789012,"PN23",1996);'
cur.execute(c)
c='insert into Titles values(3126,123466789012,"PN26",2000);'
cur.execute(c)
c='insert into Titles values(3196,143456789012,"PN31",2005);'
cur.execute(c)
d='insert into Book values(2212,3212,"Mumbai","Drama");'
cur.execute(d)
d='insert into Book values(1221,1122,"Delhi","Cool");'
cur.execute(d)
d='insert into Book values(2121,3112,"Chennai","Horror");'
cur.execute(d)
e='insert into Publishers values("ABCD123","Mohit Mehra","Tambaram",66,123000);'
cur.execute(e)
e='insert into Publishers values("ABCD122","Prabhjyot Kaur","Nungambakkam",65,124000);'
cur.execute(e)
f='insert into ZipCodes values(123000,"Delhi","Delhi",110052);'
cur.execute(f)
f='insert into ZipCodes values(456000,"muradabaad","Delhi",110000);'
cur.execute(f)
f='insert into ZipCodes values(123000,"malabar Namgar","Delhi",770052);'
cur.execute(f)
conn.commit()
print("I have inserted all the values ")

#Q.3- Update any values in any of the tables. Print the original and updated values.
conn=sqlite3.connect("riteshdb.db")
cur=conn.cursor()
a='update Book set location = "Bangalore" where bookId = 1221;'
cur.execute(a)
a='update Authors set fname = "Ducati" where authorId="Ritesh"'
cur.execute(a)
a="select * from Authors;"
cur.execute(a)
for i in cur.fetchall():
  print(i)
  

