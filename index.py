str = "apna collage"
# print(str[3])
# #string can not allow to modify
# # slining 
# print(str[3:6])
# print(str[5:len(str)]) #len(str) = balance length of string
# print(str[5:])  # [5:] = len(str)
# print(str[-4:-5])  #slicing negative index
# str = "i am a cooder and a best cooder"
# print(str.endswith("der"))
# print(str.capitalize()) # it convert first letter in capital letter
# #but not change in orginal string.
# print(str) #capitalize change only one time.
# str = str.capitalize() #now change in old string
# print(str)
# print(str.replace("o", "a")) #replace "o" into "a" in given sentance.
# print(str.replace("cooder", "docter"))
# print(str.find("o")) # give the index where word use in first time.
# print(str.count("cooder")) # count the given word use in string.
# print(str.reverse())


# marks = [96,97,89,87,76,79]
# maximum_number = max(marks)
# min_number = min(marks)
# print(maximum_number)
# print(min_number)

# li = [3,4,5,20,5,25,1,3]
# print(li.pop(1))

# def outer():
#     x=10
#     def inner():
#         x += 5
#         return x
#     return inner
# closure = outer()
# print(closure())
# print(closure())
# num1 = int(input("enter the number"))
# if num1 % 3 == 0:
#     print("Fizz")
# elif num1 % 5 == 0:
#     print("Bizz")
# elif num1 % 3 == 0 and num1 % 5 == 0:
#     print("FizzBizz")   
# else:
#     print(num1)         

# n = int(input("enter the number"))
# if n > 0:
#     for n in range(n,-1,-1):
#         print(n)
# elif n < 0:
#     for n in range(n,1,1):
#         print(n)
# else:
#     print(0)    

# n = int(input("enter the number"))
# sq = []
# for x in range(1,10):
#     sq = x*x
#     if sq <= n:
#         print(sq)


n = (1,3,4,5,3)
for i in range(len(n)):
    if(n.count >1):
        print(False)
        break
    else:
        print(True)


# n = int(input("enter the num:"))
# p = []
# for i in range(1,n):
#     if i/2 == 1 or i%2 != 0:
#         True
#     elif i/3 ==1 or i%3 !=0:
#        True   
# print(p)        





# a = int(input("enter the number"))
# b = int(input("enter the number"))
# c = a+b
# print(c)
# def calculater(a,b,opr):
#     if opr ==1:
#           print(str(a+b))
#     elif opr == 2:
#          print(str(b-a))  
#     elif opr == 3:
#          print(str(a*b))
#     else:
#          print("Invalid Input")              
# calculater(2,3,2)

# for i in range(2,34):
#      if i%2 == 0:
#           False
#      elif i%3 == 0:
#           False
#      elif i%5 ==0:
#           False
#      else:
#           True               
# print(True)          

# a = 23

# print(type(a))
# print(float(a))
# print(str(a))

 













 