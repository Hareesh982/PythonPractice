import json
import pandas as pd

file = "01_name.json"


def copy_data(x):           #copying a json data from 1 file to another
    with open('001_name.json', 'w') as file:
        json.dump(x, file, indent=4)


with open(file, 'r') as json_file:
    data = json.load(json_file)
    name_age = data['names']
    for i in name_age:
        first_name = i['first_name']
        age = i['age']
        print(f"{first_name} age is {age}")
    copy_data(data)


