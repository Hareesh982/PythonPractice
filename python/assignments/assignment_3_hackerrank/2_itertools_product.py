
from itertools import product
a = input().split()
b = input().split()

li_1 = []
li_2 = []
for i in a:
    li_1.append(int(i))
for i in b:
    li_2.append(int(i))

t = list(product(li_1, li_2))
for i in t:
    print(i, end=" ")


# ****************SAMPLE_INPUT****************

#  1 2
#  3 4

# *************OUTPUT**************

# (1, 3)(1, 4)(2, 3)(2, 4)
