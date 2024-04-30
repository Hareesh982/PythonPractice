
from itertools import combinations
s, k = input().split()
s = sorted(s)

for i in range(1, int(k) + 1):
    for x in list(combinations(s, i)):
        print(*x, sep='')


#**************SAMPLE_INPUT**************

# HACK 2

#*************OUTPUT***************

# A
# C
# H
# K
# AC
# AH
# AK
# CH
# CK
# HK
