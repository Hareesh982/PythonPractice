
from itertools import permutations
li = input().split()

value = int(li[1])
string = li[0]

string_list = []

for i in string:
    string_list.append(i)

x = permutations(string_list, value)
li = []
for i in x:
    li.append("".join(i))

li.sort()
for i in li:
    print(i)


# ****************SAMPLE_INPUT****************

# HACK 2

# ****************OUTPUT****************

# AC
# AH
# AK
# CA
# CH
# CK
# HA
# HC
# HK
# KA
# KC
# KH
