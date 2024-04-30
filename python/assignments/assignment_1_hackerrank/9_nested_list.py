# Given the names and grades for each student in a class of N students, store them in a 
# nested list and print the name(s) of any student(s) having the second lowest grade.


if __name__ == '__main__':
    n = []
    li = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        li.append([name, score])
        n.append(score)

    n.sort()
    second_min = 0
    mini = n[0]
    li.sort()
    for i in n:
        if i != mini:
            second_min = i
            break

    for i in li:
        if i[1] == second_min:
            print(i[0])


# **************SAMPLE_INPUT****************

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39

# ***************OUTPUT*****************

# Berry
# Harry
