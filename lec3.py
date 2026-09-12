# list 
# name = ["yahya" , "islam" , "mostafa" , "ali" ,"kamal" ]
# print(name[1:])
# crud application : c => create , r => read , u => update , d => delete 
names = ["yahya" , "islam" , "mostafa" , "ali" ,"kamal" ]
# create new item 
# 1- append()
# print(name)
# name.append("samar")
# # insert()
# name.insert(2 , "aboud")
# print(name)
# name = input("Enter your name :")
# indx = names.index(name) # indx = names.index("islam")
# names[indx] = "isalm dardona" #names[1] = "isalm dardona"
# print(names)

# names[0] = "yahya el saftawi"
# print(names)

# admins = ["yahya" , "islam" , "mostafa"]
# print(admins)
# admin_name = input("Enter your admin name :")
# new_admin_name = input("Enter new name :")

# admin_index = admins.index(admin_name)
# admins[admin_index] = new_admin_name
# print(admins)
curencires = ["usd" , "eur" , "jod" , "ils"]
values = [3.2 , 3.5 , 4.5 , 1.0]
input_cur = input("Enter Your currency :")
input_value = float(input("Enter your value"))
indx = curencires.index(input_cur)
cur_value = values[indx]
result = cur_value * input_value
print(f"the final result is {result} from currency {input_cur}")


# enter your currency 
# enter your amount 500
# result => 500 * 3.2 = 1500 ils