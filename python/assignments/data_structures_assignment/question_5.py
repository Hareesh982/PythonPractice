# Question-5
# Read about the Tower of Hanoi algorithm. Write a program to implement it.



def tower_of_hanoi(n, start, aux, end):
    if n == 0:
        return
    tower_of_hanoi(n-1, start, end, aux)
    print("Move disk", n, "from rod", start, "to rod", aux)
    tower_of_hanoi(n-1, end, aux, start)

n = 3
tower_of_hanoi(n, 'A', 'B', 'C')



#*********************OUTPUT*********************

# Move disk 1 from rod A to rod B
# Move disk 2 from rod A to rod C
# Move disk 1 from rod B to rod C
# Move disk 3 from rod A to rod B
# Move disk 1 from rod C to rod A
# Move disk 2 from rod C to rod B
# Move disk 1 from rod A to rod B
