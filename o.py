# f = open("dox.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

#raed only 5 text count with space.
# f = open("dox.txt","r")
# data = f.read(6)
# print(data)
# f.close()

#only read a line frome file.
# f = open("dox.txt","r")
# line1 = f.readline()
# print(line1)
# f.close()

# if pyhon can data one time than you want to read data again 
#that time curser / python can give nothing (empty line)
# f= open("dox.txt","r")
# data = f.read()
# print(data)

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# f.close()

#use "a"
# f = open("dox.txt","a")
# f.write("i want make a empair")
# f.close()

# f = open("dox.txt","a")
# f.write("\n i want to sucess")
# f.close()

#with syntax
# with open("dox.txt","r") as f:
#     data = f.read() 
#     print(data)

# with open("dox.txt","w") as f :
#     f.write("new data is here")

#delecting file
# import os
# os.remove("dox.txt")

#creat a new file "practice.txt" using python.add the following data in it:
# hi everyone
# we are learning file i/o
# using java.
# i like programming in java.

# with open("practice.txt", "w") as f:
#     f.write("hi everyone\nwe arelleraning fileI/o\nusing java\ni like programing in java")
   
#WAF THAT REPLCE ALL OCCURRENCEOF "JAVA"WITH "PHYTHON "in above file.
# with open("practice.txt","r") as f:
#     data =f.read()

# new_data = data.replace("java","python")    
# print(new_data)

# with open("practice.txt","w") as f:
#     f.write(new_data)

# search if the word "learning "existin file or not.
# word = ("learning")
# with open("practice.txt","r") as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print("found") 
#     else:
#         print("not found") 


#WAF for search word.
# def check_word():
#     word = ("python")
#     with open("practice.txt","r") as f:
#           data = f.read()
#           if(data.find(word) != -1):
#               print("found")
#           else:
#               print("not found")    

# check_word()


#WAFto find in which line of the file does the word "learnimg "occur first print -1 if word not found
# def check_for_line():
#     word = "programing"
#     data = True
#     line_no = 1 
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1
# print(check_for_line())            


#from a file containing numbersseprateted by comma ,print the count of even numbers.
count = 0 
with open("sample.txt","r") as f:
    data = f.read()

    nums = data.split(",") 
    for val in nums:
        if(int(val)% 2 == 0):
            count += 1  

print(count)    

# with open("sample.txt","r") as f:
#     data = f.read()
#     print(data)

#     num = ""
#     for i in range(len(data)):
#         if(data[i] == ","):
#             print(int(num))
#             num = ""
#         else:
#             num += data[i]    

    

    


