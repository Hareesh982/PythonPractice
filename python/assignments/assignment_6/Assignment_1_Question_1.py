import json

class Employee:

    def json_data(self):
        with open("Assignment_1_Question_1.json", 'r') as file:
            data = json.load(file)
            res = data["Employee_details"]
            list_obj = []
            for i in res:
                d = i["Name"], i["DOB"], i["Height"], i["City"], i["State"]
                list_obj.append([d])
            for i in list_obj:
                print(i)

obj = Employee()
obj.json_data()
