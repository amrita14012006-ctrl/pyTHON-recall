# name = "Amrita kumari"
# classess = "b tec"
# secation = "1f"
# university = "bty"
# print(name , classess, secation,university)


# n = int(input("enter the number"))
# while(n>=0):
#     print(n,end=" ")
#     n -= 1

# arr = tuple(map(int,input().split()))
# for i in arr:
# str = "python"
# s = len(str)
# c = s//2
# print(c,s)

n = int(input("enter the number"))
i = 2
while(i <= n-1):
    if(n%i == 0):
        print("non prime number")
        break
    i+=1
else:    
     print("prime number")   



    