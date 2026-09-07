x = 5 
y = 2
# print(abs(x))
# print(pow(x , y))
# print(x ** y)
# import math 
# a = 2.1
# print(math.ceil(a))
# print(min(10,15,2,1,52))
# zero indexing 0-> n-1 => n = length test
# name = "yahya" 
# name_list = ["y","a" ,"h" ,"y" ,"a"]
# print(name[-1])
# print(name_list[4])
# print(len(name))
# print(len(name_list))
# list1 = [1 , 2, "yahya" , True ] #list varibale conatin more than one item

name = "yahya el saftawi"
# print(name.upper())
# print(len(name))
# print(name.center(25 , "#"))
# print(name.replace("ya" , "oo"))
# print(name.split())
# list1 =['yahya', 'el', 'saftawi']
# new_name = " ".join(list1)
# print(new_name)
# print(11 % 3)
# text = "welcome for python develper"
# print(text)
# print(text.find("f"))
# yahya@gmail.com
# yahya@sfcpal.org
email = input("Enter your email :") # yahya@gmail.com
list1 = email.split("@") # ["yahya" ,"gmail.com"]
username = list1[0] # yahya
list2 = list1[1].split(".") # ["gmail" , "com"]
company = list2[0] # gmail
extention = list2[1] # com
print(f"the username is {username}")
print(f"the company is {company}")
print(f"the extention is {extention}")