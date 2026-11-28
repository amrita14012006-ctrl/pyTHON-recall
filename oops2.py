# class A:
#     varA = "welcome to class A"
# class B:
#     varB = "welcome to class B"    
# class C(A, B):
#     varC = "welcome to class C"

# c1 = C() 

# print(c1.varC)
# print(c1.varB)
# print(c1.varA) 

#use of super method.
# class Car:
#     def __init__(self,type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("car started") 
#     @staticmethod
#     def stop():
#         print("car stoped")
# class Toyota(Car):
#     def __init__(self,name,type):
#         self.name = name
#         super().__init__(type)      #super method that help to call the parents.  
# car1 = Toyota("parius","electric")
# print(car1.type)


#class method
# class Person:
#     name = "girja"

    # def changeName(self,name):
    #     Person.name = name       #change the class artibal 
 #self.__class__.name (same work as change attrubiuit ) 
 
#     @classmethod
#     def changeName(cls, name):
#         cls.name = name
         
# p1 = Person()
# p1.changeName("rahul kumar") 
# print(p1.name)       
# print(Person.name)



# class Student:
#     def __init__(self,phy,che,math):
#         self.phy = phy
#         self.che = che
#         self.math = math
#         self.percentage = str((self.phy+self.che+self.math) /3)+ "%"

#     def calcPercentage(self):
#         self.percentage = str((self.phy+self.che+self.math) /3)+ "%"    

# stu1 = Student(95,96,89)
# print(stu1.percentage) 

# stu1.phy = 89
# print(stu1.phy)
# stu1.calcPercentage()
# print(stu1.percentage)

# class Student:
#     def __init__(self,phy,che,math):
#         self.phy = phy
#         self.che = che
#         self.math = math

#     @property
#     def percentage(self):
#         return str((self.phy + self.che +self.math)/3 ) +"%"
       
# stu1 = Student(95,96,89)
# print(stu1.percentage) 

# stu1.phy = 89
# print(stu1.percentage)

#creat a complex number funcation.
# class Complex:
#     def __init__(self,real,img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real,"i +",self.img,"j")

# num1 = Complex(3 , 4)  
# num1.showNumber()      

# num2 = Complex(5 , 4)  
# num2.showNumber()  

class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")

    def add(self,num2):
        newReal = self.real +num2.real
        newImg = self.img +num2.img
        return Complex(newReal,newImg)

num1 = Complex(3 , 4)  
num1.showNumber()      

num2 = Complex(5 , 4)  
num2.showNumber()

num3 = num1.add(num2)
num3.showNumber()
