import json

with open("prac.json","r") as f:
    data = json.load(f)

p = int(input("Enter the id : "))

for i in data:
    if i["id"] == p:
        data.remove(i)


with open("prac.json","w") as f:
    data = json.dump(data,f)

