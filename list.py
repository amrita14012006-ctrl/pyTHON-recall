# marks = [54.6,85.4,65.4,84.6]
# print(marks)
# print(len(marks))
# print(type(marks))
# print(marks[3])

# student = ["ram",52.6,18,"delhi"]
# print(student[0])
# student[0] = "raman" #mutable so can change.
# print(student)

#LIST SLICING
# marks = [39,9,45,3,45,89]
# print(marks[3:5])
# print(marks[2:])
# print(marks[:-1]) #in list slicing use negative just like string slicing.
# print(marks[-6:-1])

#LIST METHODS
# list = [3,9,8]
# list.append(4) #add element in the end
# print(list)
# list.sort() #give in ascending order.
# print(list)
# list.sort(reverse=True) #in True word always T(capital t)
# print(list.sort(reverse=True)) # it return list in decending order.
# print(list)


 

# list = [3,5,8,2]
# list.insert(2,4)  #add multiple num in end.
# print(list)
# list.remove(2) #remove the given num found in first.
# print(list)
# list.pop(3) #compite remove given index num.
# print(list)


#tupl = (2,4,5,) #in last use comma symbol.
# print(tupl)
# print(type(tupl))
# tup = (4,) # if you want store single value in tuple then alyas use comma symbol.
# print(tup)
# tupm = (3,4,5,6,4,2,3,2,)
# print(tupm[1:3])
# print(tupm.index(3))
# print(tupm.count(2))

# list1 = [2,4,3]
# list2 = [5,6,4]
# sum_list = list1 + list2
# print(sum_list)

list1 = [1,3]
list2 = [2]
merget_array = list1 +list2
total = sum(list1) + sum(list2)
median = total / len(merget_array)
print("median is",median)
