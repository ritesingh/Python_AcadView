#Q.1- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.
class circle():
  def __init__(self,radius):
    self.radius = radius
  def  getArea(self):
    return 3.14*self.radius*self.radius
  def getCircumference(self):
    return self.radius*2*(22/7)
obj=circle(4)  #object creation
print(obj.getArea())   #calling member method
print(obj.getCircumference())


#Q.2- Create a Student class and initialize it with name and roll number. Make methods to : 1. Display - It should display all informations of the student.
class student():
  def __init__(self,name,roll):
    self.name = name
    self.roll= roll
  def display(self):
    print(self.name)
    print(self.roll)
obj=student("Ritesh",15)
print(obj.display())


#Q.3- Create a Temprature class. Make two methods : 1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.  2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.
class temperature():
  def  convertFahrenhiet(self,celsius):
    return (celsius*(9/5))+32
  def convertCelsius(self,farenhiet):
    return (farenhiet-32)*(5/9)
obj=temperature()
print(obj.convertFahrenhiet(12))
print(obj.convertCelsius(12))


"""Q.4- Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings .
Make methods to 
1. Display-Display the details.
2. Update- Update the movie details."""
class moviedetails():
    def __init__(self,moviename,artistname,yor,rating):
        self.moviename=moviename
        self.artistname=artistname
        self.yor=yor
        self.rating=rating
    def display(self):
        print(self.moviename,self.artistname,self.yor,self.rating,sep="\n",end="")
        return ""
    def update(self):
        self.moviename=input("enter the new movie name:")
        self.artistname=input("enter the new artist name:")
        self.yor=int(input("enter the new year of release:"))
        self.rating=int(input("enter the new rating:"))
        print("info updated!!")
        return ""
obj=moviedetails("The wolf of wallstreet","Leonardo D caprio",2013,8)
print(obj.display())
a=input("do you want to update (Y/N):")
if a=="Y" or a=="y":
    print(obj.update())
    print(obj.display())



"""Q.5- Create a class Expenditure and initialize it with expenditure,savings.Make the following methods. 
1. Display expenditure and savings 
2. Calculate total salary
3. Display salary"""
class Expenditure():
    def __init__(self,expenditure,savings):
        self.expend=expenditure
        self.savings=savings
        self.salary=""
    def display(self):
        print(self.expend,self.savings,sep="\n")
        return ""
    
    def calc(self):
        self.salary=self.expend+self.savings
        return ""

    def dispsal(self):
        if(self.salary!=""):
            print("salary is ",self.salary)
        else:
            print("first calculate salary")
        return ""
    
exp=int(input("enter the expenditure:"))
sav=int(input("enter the savings:"))        
obj=Expenditure(exp,sav)
ch=int(input("1.Display Expenditure and Savings\n2.Calculate Salary\n3.Display salary.\nEnter your choice"))
if ch==1:
        obj.display() 
elif ch==2:
        obj.calc()
        obj.dispsal()
elif ch==3:
        obj.dispsal()
else:
        print("wrong choice!!")

        
        
       










