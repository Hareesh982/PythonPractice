import json

def write(data,filename = "01_name.json"):
    with open(filename,'w') as file:
        json.dump(data,file,indent=4)

def validation(first_name,age):
    if(len(age)>100):
        print("Enter a valid age")

with open("01_name.json") as json_file:
    data = json.load(json_file)
    temp = data['names']
    first_name = input("Enter the name : ")
    age = int(input("Enter the age : "))
    validation(first_name,age)
    new_data = {"first_name" : f"{first_name}","age" : f"{age}"}
    temp.append(new_data)
    write(data)
    