from collections import deque

li = [1,2,3,4,5]
d = deque(li)

d.append(6)
print("append [6] : ",d)

d.appendleft(7)
print("append left [7] : ",d)

d.extend([8,9,10])
print("extend [8,9,10] : ",d)

d.extendleft([11,12,13])
print("extend left [11,12,13] : ",d)

d.pop()
print("pop : ",d)

d.popleft()
print("pop left : ",d)

