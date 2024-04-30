# Consider a list(list=[]). You can perform the following commands:

# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.


if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        li = list(input().split())
        if li[0] == 'insert':
            l.insert(int(li[1]), int(li[2]))
        elif li[0] == 'remove':
            l.remove(int(li[1]))
        elif li[0] == 'append':
            l.append(int(li[1]))
        elif li[0] == 'sort':
            l.sort()
        elif li[0] == 'pop':
            l.pop()
        elif li[0] == 'reverse':
            l.reverse()
        elif li[0] == 'print':
            print(l)


#****************SAMPLE_INPUT******************

# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

#***************OUTPUT****************

# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]
