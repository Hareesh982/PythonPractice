import json

d = {
    "Madhya Pradesh": "Bhopal",
    "Karnataka" : "Bangalore",
    "Telangana" : "Hyderabad",
    "West Bengal" : "Kolkata",
    "Tamilnadu" : "Chennai",
    "Maharastra" : "Mumbai",
    "Rajasthan" : "Jaiput",
    "Goa": "Panaji"
}

with open("Assignment_2_Question_2.json",'w') as file:
    json.dump(d,file,indent=4)
