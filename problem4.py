# store following word meaning in python dictonary:
# table: "a pice of firniture","list of facts & figures"
# cat : "a small animal"

# dict ={
#    "table" : ["a pice of furniture" ,"list of fact & figure"],
#    "cat" : "a small animal"
# }
# print(dict)

# you are given a list of subjects for students. assume one classroom
# is requre for 1 subject . how many classroom are needed by all students.
# "python","java","javascript","c++","c","java","python","java"

# classroom = {"python","java","javascript","c++","c","java","python","java"}
# print(len(classroom))


# WAP to enter marks of 3 subjects from the user and store them in a dictinory.
# start with an empty dictonary & add one by one . use subject name as key & marks as
# value. 

# null_dict ={}
# first = int(input("enter the num of math"))
# second = int(input("enter the num of science"))
# third = int(input("enter the num of histrory"))
# null_dict["marks1"] = first
# null_dict["marks2"] = second
# null_dict["marks3"] = third
# print(null_dict)

# marks = {}
# x = int(input("enter phy:"))
# marks.update({"phy":x})

# x = int(input("enter che:"))
# marks.update({"che": x})

# x = int(input("enter math"))
# marks.update({"math": x})

# print(marks)


# figure out a way to store 9 & 9.0 as seprate value in 
# the set (you can take help of built in data type)

def insert_dict(query, d):
    dict[query[1]] = int(query[2])
    print( "Inserted") 
    # Your code here
    
# deleting from dictionary
def del_dict(query, d):
    if query[1] in d:
        del d[query[1]]
        print("Delected")
    else:
        print("-1")
    # Your code here
# print marks of required name
def print_dict(key, d):
    if key in d:
        print(f"Marks of {key} is {d[key]}")
    else:
        print("-1")
    # Your code here
n = int(input())
d = {}
for _ in range(n):
    query = input().split()
    if query[0] == 'i':
        insert_dict(query,d)
    elif query[0] == 'd':
        del_dict(query , d)
    elif query[0] == 'p':
        print_dict(query[1],d)



