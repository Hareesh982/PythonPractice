# with counter

from collections import Counter

li = [1,2,3,2,4,5,2,1,3,4,2,1,1,1,3,4]
print(Counter(li))

print(Counter(a=2,b=3,c=4))

# without counter

s = set(li)
d = dict()
for i in s:
    d[i] = li.count(i)
print(d)
