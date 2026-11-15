# def show(n):
#     if(n == 0):  #base case that decide to where recursion stop.
#         return
#     print(n)
#     show(n-1) 

# show(5 )    


# def fact(n):
#     if(n == 1 or n==0):
#         return 1
#     return fact(n-1) * n

# print(fact(5))        

#write a recursive funcation the sum of first n natural numbers.
# def cal_sum(n):
#     if(n == 0):
#         return 0
#     return cal_sum(n-1) + n

# sum = cal_sum(5)  
# print(sum)     

#write a recursive funcation to print all elements in a list.
#hint: use list & index as parameters.
def print_list(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])   
    print_list (list,idx+1)

name = ["radha","brajraj","vrindavan"]   
print_list(name) 
