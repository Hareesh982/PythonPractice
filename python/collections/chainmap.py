from collections import ChainMap

d1 = {"name" : "hareesh", "age" : 23}
d2 = {"name" : "rajesh", "age" : 21}
d3 = {"name" : "asha" , "age" : 23}

add = ChainMap(d1,d2,d3)
print(add)

#adding a new dictionary

d4 = {"name" : "rajendra" , "age" : 19}
new_add = add.new_child(d4)
print(new_add)

#deleting a key
#deletion is possible only for first index of chainmap

del new_add["name"]
print(new_add)



