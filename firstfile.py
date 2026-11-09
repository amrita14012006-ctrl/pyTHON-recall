# #WAAP to prime numbbers upto n which are not divisible by 3,6,9
# n = int(input("enter the number:"))
# i = 1
# # while i <= n:
# #     if(i%3 == 0):
# #         print("divded by 3") 

# #     i+=1
# #     print(i)
# print(n*1)
# print(n*2)

#write a programe to reverse a given string.
# str = "hellow"
# print("reversed string:",str[::-1])

#write  programe to count the number of vowels in a string.
# s = input("enter the sstring")
# vowel = "aeiou"
# count = 0
# for ch in s:
#     if ch in vowel:
#         count+=1
# print("vowel in string is ",count)
#write a programe to check whether a string is a palidrome or not.
# st = input("enter the string")
# st1 = input("enter the second string")
# if(st[::-1] == st1[::-1]):
#     print("palidrom string")
# else:
#     print("not palidrome string")  


#write a programe to remove all space frome a string.
# s = input("enter the string")
# print("remove space",s.replace(" ",""))


#write a programe to check whether two string are anagrams(both side have same characters)
#input: "listen", "silent"
# s1 = input("enter the first string")
# s2 = input("enter the ssecond string")
# if sorted(s1) == sorted(s2):
#     print("anagrams")
# else:
#     print("not anagrams")

#str = "hellow i am a student"
#(str.upper())
# str1 = "WE ARE FOLLISH"
# print(str1.lower())
# print(str1.count("E")) 
# print(len(str1))
# print(str.replace("hellow", "CULTURAL"))
#print(str.count(" ") + 1)
# i = 14
# while <= len(str):
#     print(str[i])
#     i-=1

#print each charecter with index:
# s = input("enter a string")
# index = 0
# while index < len(s):
#     print(index , s[index])
#     index +=1

#count frequency of each charecter:
# s = input("enter a string")
# freq = {}
# for char in s:
#     if char in freq:
#         freq[char]+=1
#     else:    
#         freq[char] = 1
# for key in freq:
#     print(key," ",freq[key])  

#first non repeating character:
# s = input("enter a string")
# for ch in s:
#     count = 0
#     for c in s:
#         if ch == c:
#             count+=1
#     if count == 1:
#         print("first non repeateding char is",ch)   
#         break     

#remove duplicate character:
# s = input("enter a string")
# result = " "
# for ch in s:
#     if ch not in result :
#         result += ch
# print("after removing duplicate:",result)        

#reverse word in sentance:
# s = input("enter a sentence:")
# words = s.split()
# rev = " "
# for i in range(len(words)-1,-1,-1):
#     rev += words[i] + ""
# print("reverse words",rev)    

#find the longest word:
# s = input("enter sentence")
# words = s.split()
# longest = words[0]
# for w in words:
#     if len(w) > len(longest):
#         longest = w
# print("longest word is ",longest)        

#check vaild password:
# pas = input("enter the password")
# has_upper = False
# has_digit = False
# if len(pas)< 8 :
#     print("invalid password")
# else:
#     for ch in pas:
#         if ch.isupper():
#             has_isupper = True
#         if ch.isdigit():    
#             has_isdigit() = True
#     if has_upper and has_digit:
#         print("valid password") 
#     else:
#         print("invalid password")  

# s = input("enter a string")
# vowel = "aeiou"
# count = 0
# for ch in s:
#     if ch not in vowel:
#         count+=1
# print("count of consonants",count)        
# print(len(s))

# s = input("enter a string")
# for ch in s:
#     if ch is int:
#         print(True)
#     else:
#         print(False)  
#         break          

#capitalize first letter of each word:
# s = input("enter string")
# words = s.split()
# result = " "
# for w in s:
#     result += w[0].upper()+w[1:]+""
# print("result",result) 

#swap of first character and last character
# s = input("enter string")
# if len(s) <= 1:
#     print("result",s)
# else:
#     result = s[-1]+s[1:-1]+s[0]   
#     print("after swap",result) 

#check if string contains only digits
# s = input("enter string")
# is_digit = True
# for ch in s :
#     if ch<'0' or ch<'9':
#         is_digit = False
#         break
# if is_digit :
#     print("string contains only")   
# else:
#     print("string does not contain only digit")  

# s = input("enter string")
# vowel = "aeiouAEIOU"  
# count = 0
# for ch in s:
#     if ch.isalpha() and ch not in vowel:
#         count+=1
# print("Number of consonants:",count)  

# s = input("enter a string")
# vowel = 'aeiouAEIOU'
# for ch in s:
#     if ch not in vowel:
#         print(ch)


s = input("enter a sentence")
words = s.split()
smallest = word[0]
for w in words:
    if len(w)<len(smallest):
        smallest = w
print("smallest word is longest",smallest)        