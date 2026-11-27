# class student:     #class = variable ,  student = class name
#     name = "radha"   

# #object
# s1 = student()   #s1 = object varible name,  student = class name
# print(s1.name)    

#class is created
# class car:                #class = varible name, car = class name
#     colour = "yellow"   
#     brand = "rj"

# car1 = car()          #car1 = object varible name
# print(car1.colour)
# print(car1.brand)
    
# class student:
#     name = "mirabai" 
#     def __init__(self):
#         print(self)
#         print("adding new student in database")
    
# s1 = student()
# print(s1.name)       

# class student:

#     #default construcations
#     def __init__(self, name):
#         print("adding new student in database")

# #parameterized construcations.
#     def __init__(self, name,marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in database")

# s1 = student("kabirdas" , 89)    
# print(s1.name,s1.marks)


# s2 = student("madav",94)
# print(s2.name,s1.marks)

# class Student:
#     collage_name = "ABC collage"
#     name = "anonymous"  #class attru

#     def __init__(self,name,marks):
#         self.name = name  #obj attr > class attru
#         self.marks = marks
#         print("adding new student in database")


# s1 = Student("radhraman", 100)
# print(s1.name)

# class Student:
#     collage_name = "Abc collage"

#     def __init__(self,name, marks):
#         self.marks = marks
#         self.name = name

#     def welcome(self):
#         print("welcome student",self.name)

#     def get_marks(self):
#         return self.marks   

# s1 = Student("radh",100)
# s1.welcome()        

# creat student class that takes name &marks of 3 subjects
# as argument in constuctor then create a method to print the average.

# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi",self.name,"your avg score is",sum/3)  

# s1 = Student("gopi",[96,95,84])
# s1.get_avg()

# s1.name = "brinda"
# s1.get_avg()


# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.cluth = False

#     def Start(self):
#         self.cluth  = True
#         self.acc = True  
#         print("car started..")  

# car1 = Car()
# car1.start()        

# creat account class with 2 attrivutes - balance and account no.
# create mrthod for debit,credit & printing the balance.

# class Account:
#     def __init__(self,bal,acc):
#         self.balance = bal
#         self.account_no = acc

#     def debit(self,amount):
#         self.balance -= amount
#         print("Rs.",amount ,"was debited")  
#         print("total balance = ",self.get_balance())

#     def cridet(self,amount):
#         self.balance += amount
#         print("Rs.",amount,"was crideted")
#         print("total balnce = ",self.get_balance()) 

#     def get_balance(self):
#         return self.balance

# acc1 = Account(10000,123654)
# acc1.debit(1000)
# acc1.cridet(500)

#del keyword use
# class Student:
#     def __init__(self,name):
#         self.name = name


# s1 = Student("amrita")
# print(s1.name)
# del s1
# print(s1.name)



#this code is not safe for account pass.
#because you can print the password
# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.acc_pass = acc_pass

# acc1 = Account("12345","abcd")   
# print(acc1.acc_no)

#this code is safe for pass. it only in the class not outside.
# class Account:
#     def __init__(self,acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass   #private  attributes.

#     def reset_pass(self):
#         print(self.__acc_pass)

# acc1 = Account("123456","abcdef")

# print(acc1.acc_no)
# print(acc1.reset_pass())

# class Person:
#     __name = "radharaman"

#     def __hello(self):
#         print("hello person")

#     def welcome(self):
#         self.__hello()  

# p1 = Person() 

# print(p1.welcome()) 

#INHERITANCE
# class Car:
#     @staticmethod
#     def start():
#         print("car started")

#     @staticmethod
#     def stop():
#         print("car stoped")   

# class ToyatoCar(Car):  #pass all funcation in this funcation from car funcation.
#     def __init__(self,name):
#         self.name = name

# car1 = ToyatoCar("fortuner")
# car2 = ToyatoCar("perius")   

# print(car1.start())

class Car:
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stoped") 

class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name

class Fortuner(ToyotaCar):
    def __init__(self,brand):
        self.brand =    brand            

car1 = Fortuner("red")
car1.start()
