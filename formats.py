import json

f  = open('people.json')

json_data = f.read()

user_list = json.loads(json_data)
count_male = 0
count_female = 0
for user in user_list:
    if user["gender"] == "Male":
         count_male +=1
    if user["gender"] == "Female":
        count_female +=1
print("Erkakalar soni:",count_male,"ta")
print("Ayollar soni: ",count_female,"ta")
print("\n")
print("Hindistonlik foydalanuvchilar")
for user in user_list:
    if user["country"] == "India":
        print(user)
print("\n")
print("20 yoshdan kichik foydalanuvchilar")
for user in user_list:
    if user["age"] < 20:
        print(user)
print("\n")
print("Muhandislar")
for user in user_list:
    if user["job"] == "Engineer":
        print(user)