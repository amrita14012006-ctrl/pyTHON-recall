#DICTONARY AND SET
# info = {
#     "name": "virdhavan",
#     "subjects" : ["python","c language","java"],
#     "topic": ("cict","set"),
#     "age": 37,
#     "is_adult":True,
# }
# print(info) 
# print(type(info))
# print(info["name"])
# print(info["subjects"])
# info["name"] = "radharaman"  #assine vale and oid value overwrite.
#print(info)
# null_dict = {}                #we can make a null dict .and with time we can creat something in this dict.
# null_dict["name"] = "apna"
# print(null_dict)
 #in dict we can use every variable,string,list,
#tuple,bollen that can change and we can make key that type 
# which can not change. like tuple

student = {
    "name" : "virshbhanu ki dulari",
   "subject" : {
    "phy" : 95,
    "che" : 98,
    "math": 99,

   }
}
#nested dictonary
# print(student["subject"]["math"])
# print(len(student))  #total length of dict.
# print(list(student.keys()))  #convert into list.
# print(len(list(student.keys())))  #length of list.
# print(student.values())
# print(list(student.values()))  
print(student["name"])     #if in this line get change than give error.
print(student.get("name"))  #if in this line get change than give none .
print(student.get('name2'))  #it print none.
#student.update({"city":"delhi"}) #add new value.
new_dict = {"city":"delhi","age": 16}
student.update(new_dict)  #add multiple values.
print(student)

